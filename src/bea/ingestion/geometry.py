from dataclasses import dataclass
from typing import Any

import pandas as pd

from bea.domain.models import Frequency

LINE_ROW = 7
DESCRIPTION_COL = 1
SERIES_CODE_COL = 2
VALUE_START_COL = 3
DATA_START_ROWS: dict[Frequency, int] = {
    Frequency.ANNUAL: 8,
    Frequency.QUARTERLY: 9,
    Frequency.MONTHLY: 9,
}


@dataclass(frozen=True, slots=True)
class ParsedSheet:
    metadata: dict[str, str | None]
    frequency: Frequency
    observations: list[dict[str, Any]]


def clean(value: Any) -> str | None:
    if pd.isna(value):
        return None
    text = str(value).strip()
    if not text or text.lower() == "nan":
        return None
    return text


def parse_metadata(df: pd.DataFrame) -> dict[str, str | None]:
    return {
        "table_title": clean(df.iat[0, 0]),
        "table_note": clean(df.iat[1, 0]),
        "coverage_note": clean(df.iat[2, 0]),
        "source_agency": clean(df.iat[3, 0]),
        "published_at_raw": clean(df.iat[4, 0]),
        "file_created_at_raw": clean(df.iat[5, 0]),
    }


def detect_frequency(df: pd.DataFrame) -> Frequency | None:
    if len(df.index) < 3 or len(df.columns) == 0:
        return None
    coverage = clean(df.iat[2, 0])
    if coverage is None:
        return None
    for prefix, frequency in (
        ("Annual data", Frequency.ANNUAL),
        ("Quarterly data", Frequency.QUARTERLY),
        ("Monthly data", Frequency.MONTHLY),
    ):
        if coverage.startswith(prefix):
            return frequency
    return None


def parse_periods(
    df: pd.DataFrame, frequency: Frequency
) -> list[tuple[int, str]]:
    periods: list[tuple[int, str]] = []
    for col_idx in range(VALUE_START_COL, len(df.columns)):
        try:
            year = int(df.iat[LINE_ROW, col_idx])
            if frequency is Frequency.ANNUAL:
                period = str(year)
            else:
                sub = int(df.iat[LINE_ROW + 1, col_idx])
                if frequency is Frequency.QUARTERLY:
                    period = f"{year}Q{sub}"
                else:
                    period = f"{year}M{sub:02d}"
        except (TypeError, ValueError, IndexError):
            continue
        periods.append((col_idx, period))
    return periods


def build_observations(
    df: pd.DataFrame,
    metadata: dict[str, str | None],
    provenance: dict[str, str],
    frequency: Frequency,
) -> list[dict[str, Any]]:
    periods = parse_periods(df, frequency)
    start_row = DATA_START_ROWS[frequency]
    observations: list[dict[str, Any]] = []
    for row_idx in range(start_row, len(df)):
        line_description = clean(df.iat[row_idx, DESCRIPTION_COL])
        if line_description is None:
            break
        line_number = clean(df.iat[row_idx, 0])
        series_code = clean(df.iat[row_idx, SERIES_CODE_COL])
        values = pd.to_numeric(
            df.iloc[row_idx, VALUE_START_COL:], errors="coerce"
        )
        for col_idx, period in periods:
            value = values.iloc[col_idx - VALUE_START_COL]
            if pd.isna(value):
                continue
            observations.append(
                {
                    **metadata,
                    "frequency": frequency.value,
                    "line_number": line_number,
                    "line_description": line_description,
                    "series_code": series_code,
                    "period": period,
                    "value": float(value),
                    **provenance,
                }
            )
    return observations
