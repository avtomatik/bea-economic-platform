# BEA Economic Data Platform

A portfolio-grade reference architecture for ingesting historical U.S. Bureau of Economic Analysis (BEA) releases, preserving source provenance, normalizing economic observations, and building analytical datasets.

This repository is deliberately technology-neutral at the architectural level. The current implementation is a Python reference implementation whose purpose is to establish semantics, data contracts, and test fixtures. A later Scala/Spark implementation can replace individual layers without changing the domain model.

## Design principles

- Preserve source evidence and provenance.
- Treat historical releases as vintages, not merely as duplicate files.
- Keep the spreadsheet-geometry parser explicit and testable.
- Separate raw extraction from canonical analytical modeling.
- Keep orchestration outside ingestion and transformation code.
- Keep DuckDB as the local analytical reference engine; benchmark alternatives against real workloads before adopting them.
- Introduce Scala only where a concrete engineering problem justifies it.

## Current flow

```text
BEA release archive
    |
    v
source artifact inventory
    |
    v
Excel geometry parser
    |
    v
raw observations + provenance
    |
    v
canonical staging
    |
    v
analytical warehouse / marts
```

## Repository layout

```text
src/bea/domain/          Domain objects and canonical concepts
src/bea/ingestion/       Archive + Excel parsing, including spreadsheet geometry
src/bea/storage/         DuckDB persistence and schemas
src/bea/transformation/  Canonicalization and analytical transformations
src/bea/analytics/       User-facing economic questions / metrics
src/bea/application/     Thin application entry points

docs/domain/             Extracted BEA domain knowledge
docs/architecture/      Architecture and ADRs
conf/sources/            Dataset-specific source configuration
data/external/          Downloaded archives (not committed)
data/raw/               Raw/bronze outputs (not committed)
data/staging/            Canonical staging outputs (not committed)
data/warehouse/          Analytical database / materializations

tests/                   Unit and integration tests
scala/                   Target architecture and migration notes
```

## Quick start

```bash
uv sync
uv run pytest
uv run bea-ingest --source-dir data/external --db data/warehouse/bea.duckdb
```

The default command scans ZIP archives in `data/external` and writes the raw observation layer plus ingestion failures to DuckDB.

## What is intentionally not here

The old experimental `src/main.py` series probes and network helpers are not carried forward. Their useful information has been extracted into domain documentation and source configuration.
