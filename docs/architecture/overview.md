# Architecture overview

## Logical layers

1. **Source** — BEA releases and downloaded artifacts.
2. **Ingestion** — archive inspection, workbook loading, spreadsheet geometry parsing.
3. **Raw** — evidence-preserving extracted observations plus ingestion failures.
4. **Staging** — canonical types, normalized series and periods.
5. **Warehouse/marts** — dimensional facts and analytical aggregates.
6. **Serving** — API, dashboard, reports.
7. **Orchestration** — schedules and dependency management around the pipeline.

## Boundary rule

Ingestion code should not depend on orchestration. Storage should not know Excel geometry. Analytics should not know ZIP internals.

## Current technology choices

The reference implementation uses Python + pandas for source parsing and DuckDB/Arrow for local analytical storage. This is intentionally a baseline, not an architectural commitment.

The next technology decision should be workload-driven:

- Parquet: portable analytical interchange/object storage layer.
- DuckDB: local analytical engine and test reference.
- ClickHouse/Pinot: only after serving/query workloads demonstrate a need.
- Spark/Scala: only after transformation scale or learning objectives justify distributed/strongly-typed processing.
- Dagster: orchestration/lineage once the asset graph is stable.
