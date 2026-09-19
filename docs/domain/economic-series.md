# Economic series

A series is the conceptual time series being measured.

Core attributes:

- `series_code`: source-provided identifier when available.
- `description`: human-readable series/line description.
- `dataset`: logical BEA dataset.
- `frequency`: annual, quarterly, or monthly in the current source family.
- `unit`: reserved for canonical metadata enrichment.
- `concept`: reserved for analytical taxonomy/enrichment.

Series metadata belongs in a dimension or canonical registry, not repeated verbatim in every analytical fact row.
