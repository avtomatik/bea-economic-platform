# ADR 0002: Scala is a later implementation experiment

## Decision

Do not make Scala the first implementation rewrite.

First establish domain contracts, parsing semantics, canonical models, tests, and workload benchmarks in the reference implementation.

## Rationale

A language migration without a demonstrated problem teaches little about architecture. Scala becomes meaningful when it is introduced for one or more concrete reasons such as a distributed Spark transformation stage, type-safe domain modeling at scale, or the explicit learning objective of comparing implementations.

## Consequence

The Python implementation must expose clean seams so that a later Scala/Spark implementation can replace ingestion or transformation without changing the conceptual data contracts.
