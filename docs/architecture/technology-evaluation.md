# Technology evaluation criteria

| Technology | Use when | Do not introduce when |
|---|---|---|
| DuckDB | local analytical SQL, reproducibility, batch exploration | a distributed serving requirement is proven |
| Parquet | portable columnar storage, object storage, engine interchange | source evidence itself needs to remain in original format |
| ClickHouse | high-throughput analytical serving and large aggregations | local batch analytics already meet the workload |
| Apache Pinot | low-latency slice-and-dice serving with real-time-ish ingestion | workload is predominantly offline batch |
| Spark | distributed transformations or very large datasets | one workstation can comfortably process the data |
| Dagster | orchestration, lineage, schedules, retries, observability | pipeline boundaries are still unstable |
| dbt | SQL-centric warehouse transformations and tests | transformation logic is mostly procedural/source parsing |
| Scala | a concrete need for typed JVM processing, Spark, or the learning objective | merely to rewrite existing Python |
