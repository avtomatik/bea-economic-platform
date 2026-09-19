# ADR 0001: DuckDB is the reference analytical engine

## Decision

Use DuckDB as the initial local analytical reference engine.

## Rationale

The current dataset is analytical, batch-oriented, and locally reproducible. No distributed execution requirement has yet been demonstrated.

## Consequence

The storage boundary must avoid DuckDB-specific semantics where practical. Parquet can become the portable interchange layer, allowing later evaluation of ClickHouse or other engines using the same datasets and workload queries.
