import duckdb


def revision_query() -> str:
    """Return a reusable query comparing values across historical releases."""
    return """
    SELECT
        series_code,
        period,
        MIN(value) AS min_value,
        MAX(value) AS max_value,
        MAX(value) - MIN(value) AS absolute_revision_range
    FROM canonical.fact_observation
    GROUP BY series_code, period
    """


def run_revision_summary(con: duckdb.DuckDBPyConnection):
    return con.sql(revision_query())
