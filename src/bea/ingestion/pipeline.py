import logging
import time
from pathlib import Path

from bea.ingestion.excel import iter_archive_sheets, parse_sheet
from bea.storage.duckdb import (connect, create_raw_tables, insert_failure,
                                insert_observations)

LOG = logging.getLogger(__name__)


def ingest_directory(
    source_dir: Path, db_path: Path
) -> dict[str, int | float]:
    started = time.perf_counter()
    inserted = 0
    failures = 0
    archives = 0
    with connect(db_path) as con:
        create_raw_tables(con)
        for archive_path in sorted(source_dir.glob("*.zip")):
            archives += 1
            LOG.info("archive=%s", archive_path.name)
            for source_file, sheet, error in iter_archive_sheets(archive_path):
                if error is not None:
                    failures += 1
                    insert_failure(
                        con,
                        {
                            "source_archive": archive_path.name,
                            "source_file": source_file,
                            "source_sheet": None,
                            "error_message": str(error),
                        },
                    )
                    continue
                assert sheet is not None
                excel, sheet_name = sheet
                provenance = {
                    "source_archive": archive_path.name,
                    "source_file": source_file,
                    "source_sheet": sheet_name,
                }
                try:
                    rows = parse_sheet(excel, sheet_name, provenance)
                    inserted += insert_observations(con, rows)
                except Exception as exc:  # noqa: BLE001 - isolate bad sheets
                    failures += 1
                    insert_failure(
                        con,
                        {**provenance, "error_message": str(exc)},
                    )
                    LOG.exception(
                        "failed sheet=%s file=%s", sheet_name, source_file
                    )
    return {
        "archives": archives,
        "observations": inserted,
        "failures": failures,
        "elapsed_seconds": time.perf_counter() - started,
    }
