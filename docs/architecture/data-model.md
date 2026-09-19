# Data model

## Raw

`raw.bea_observations` remains close to the source extraction shape. It answers: "what exactly did we extract?"

## Canonical staging

Target canonical entities:

```text
dim_dataset
dim_release
dim_source_artifact
dim_series
dim_period
fact_observation
```

The fact row is intentionally narrow:

```text
series_id
period_id
release_id
value
```

The historical release dimension is critical because BEA values can be revised across vintages.

## Analytical marts

Examples should be driven by user questions rather than source tables:

- GDP contribution/decomposition
- investment growth
- industry growth
- revision analysis
- economic-cycle indicators
