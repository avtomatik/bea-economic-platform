from collections.abc import Iterable
from pathlib import Path

import duckdb
import pyarrow as pa

RAW_SCHEMA = "raw"


def connect(db_path: Path) -> duckdb.DuckDBPyConnection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(db_path))


def create_raw_tables(con: duckdb.DuckDBPyConnection) -> None:
    con.execute(f"CREATE SCHEMA IF NOT EXISTS {RAW_SCHEMA}")
    con.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {RAW_SCHEMA}.bea_observations (
            table_title TEXT,
            table_note TEXT,
            coverage_note TEXT,
            source_agency TEXT,
            published_at_raw TEXT,
            file_created_at_raw TEXT,
            frequency TEXT,
            line_number TEXT,
            line_description TEXT,
            series_code TEXT,
            period TEXT,
            value DOUBLE,
            source_archive TEXT,
            source_file TEXT,
            source_sheet TEXT
        )
        """
    )
    con.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {RAW_SCHEMA}.bea_ingestion_failures (
            source_archive TEXT,
            source_file TEXT,
            source_sheet TEXT,
            error_message TEXT
        )
        """
    )


def insert_observations(
    con: duckdb.DuckDBPyConnection, observations: Iterable[dict]
) -> int:
    rows = list(observations)
    if not rows:
        return 0
    table = pa.Table.from_pylist(rows)
    con.register("_bea_batch", table)
    try:
        con.execute(
            f"""
            INSERT INTO {RAW_SCHEMA}.bea_observations
            SELECT table_title, table_note, coverage_note, source_agency,
                   published_at_raw, file_created_at_raw, frequency,
                   line_number, line_description, series_code, period,
                   value, source_archive, source_file, source_sheet
            FROM _bea_batch
            """
        )
    finally:
        con.unregister("_bea_batch")
    return len(rows)


def insert_failure(
    con: duckdb.DuckDBPyConnection, failure: dict[str, str | None]
) -> None:
    con.execute(
        f"INSERT INTO {RAW_SCHEMA}.bea_ingestion_failures VALUES (?, ?, ?, ?)",
        [
            failure.get("source_archive"),
            failure.get("source_file"),
            failure.get("source_sheet"),
            failure.get("error_message"),
        ],
    )
