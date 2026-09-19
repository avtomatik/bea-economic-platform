from pathlib import Path
from zipfile import ZipFile

import pandas as pd

from bea.ingestion.geometry import (build_observations, detect_frequency,
                                    parse_metadata)


def iter_archive_sheets(archive_path: Path):
    with ZipFile(archive_path) as archive:
        for member in archive.filelist:
            if member.is_dir():
                continue
            try:
                excel = pd.ExcelFile(archive.open(member.filename))
            except (
                Exception
            ) as exc:  # noqa: BLE001 - failure is part of batch semantics
                yield member.filename, None, exc
                continue
            for sheet_name in excel.sheet_names:
                yield member.filename, (excel, sheet_name), None


def parse_sheet(
    excel: pd.ExcelFile, sheet_name: str, provenance: dict[str, str]
) -> list[dict]:
    df = pd.read_excel(excel, sheet_name=sheet_name, header=None)
    frequency = detect_frequency(df)
    if frequency is None:
        return []
    metadata = parse_metadata(df)
    return build_observations(df, metadata, provenance, frequency)
