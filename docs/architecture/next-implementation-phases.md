# Next implementation phases

## Phase 1 — reference ingestion

Complete the parser contract against real archived workbooks. Add fixtures for annual, quarterly, and monthly sheets, including malformed sheets and non-data sheets.

## Phase 2 — canonical warehouse

Create `dim_dataset`, `dim_release`, `dim_source_artifact`, `dim_series`, `dim_period`, and `fact_observation`. Preserve release/vintage identity.

## Phase 3 — Parquet

Materialize canonical datasets to Parquet and make DuckDB query those datasets directly where practical.

## Phase 4 — analytics

Implement marts around user questions: GDP decomposition, industry growth, investment, and vintage revisions.

## Phase 5 — orchestration

Introduce Dagster only once the asset graph is stable. Keep asset bodies independent of Dagster.

## Phase 6 — workload benchmark

Build a representative query suite and measure DuckDB against candidate serving engines. Include data volume, query latency, refresh pattern, and operational complexity.

## Phase 7 — Scala

Reimplement one bounded stage in Scala first. A strong candidate is the canonical transformation stage or a Spark-backed batch transformation once the dataset/workload justifies it. Compare semantics and performance against the reference implementation.
