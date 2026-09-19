from pathlib import Path

from bea.storage.duckdb import connect, create_raw_tables, insert_observations


def test_duckdb_raw_insert(tmp_path: Path):
    db = tmp_path / "test.duckdb"
    with connect(db) as con:
        create_raw_tables(con)
        count = insert_observations(
            con,
            [
                {
                    "table_title": "GDP",
                    "table_note": None,
                    "coverage_note": "Annual data",
                    "source_agency": "BEA",
                    "published_at_raw": None,
                    "file_created_at_raw": None,
                    "frequency": "annual",
                    "line_number": "1",
                    "line_description": "GDP",
                    "series_code": "A191RC1",
                    "period": "1929",
                    "value": 103.6,
                    "source_archive": "a.zip",
                    "source_file": "a.xls",
                    "source_sheet": "Sheet1",
                }
            ],
        )
        assert count == 1
        assert (
            con.execute(
                "select count(*) from raw.bea_observations"
            ).fetchone()[0]
            == 1
        )
