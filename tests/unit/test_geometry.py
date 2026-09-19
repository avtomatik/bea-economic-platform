import pandas as pd

from bea.domain.models import Frequency
from bea.ingestion.geometry import build_observations, detect_frequency, parse_periods


def make_annual_frame():
    rows = [[None] for _ in range(10)]
    rows[0] = ["GDP"]
    rows[1] = ["note"]
    rows[2] = ["Annual data 1929-1931"]
    rows[3] = ["U.S. Bureau of Economic Analysis"]
    rows[4] = ["published"]
    rows[5] = ["created"]
    rows[7] = [None, None, None, 1929, 1930, 1931]
    rows[8] = ["1", "Gross domestic product", "A191RC1", 103.6, 108.7, 112.1]
    rows[9] = [None, None, None, None, None, None]
    return pd.DataFrame(rows)


def test_detect_annual_frequency():
    assert detect_frequency(make_annual_frame()) is Frequency.ANNUAL


def test_parse_annual_periods():
    periods = parse_periods(make_annual_frame(), Frequency.ANNUAL)
    assert [p for _, p in periods] == ["1929", "1930", "1931"]


def test_build_observations_is_long_format():
    df = make_annual_frame()
    rows = build_observations(
        df,
        {
            "table_title": "GDP",
            "table_note": "note",
            "coverage_note": "Annual data 1929-1931",
            "source_agency": "BEA",
            "published_at_raw": "published",
            "file_created_at_raw": "created",
        },
        {
            "source_archive": "release.zip",
            "source_file": "table.xls",
            "source_sheet": "50900 Ann",
        },
        Frequency.ANNUAL,
    )
    assert len(rows) == 3
    assert rows[0]["series_code"] == "A191RC1"
    assert rows[1]["period"] == "1930"
    assert rows[2]["value"] == 112.1
