# Orchestration

The intended Dagster asset graph is:

```text
source_archives
      |
raw_observations
      |
canonical_series + canonical_periods
      |
fact_observation
      |
economic_marts
      |
serving_outputs
```

Dagster should provide scheduling, retries, lineage, materialization history, observability, and data-quality checks. The assets themselves should remain callable without Dagster.
