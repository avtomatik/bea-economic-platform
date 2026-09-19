# Scala migration target

This directory intentionally contains architecture guidance rather than an artificial Scala rewrite.

The target separation is:

```text
bea-domain
bea-parser
bea-transform
bea-storage
bea-app
```

Recommended first experiment:

1. Keep source ZIP/Excel acquisition and storage contracts unchanged.
2. Implement the canonical period/series transformation in Scala.
3. If scale warrants it, run the transformation through Spark.
4. Compare row-level results against the Python reference implementation.
5. Promote Scala only after a measurable reason exists.

Potential Scala technologies to evaluate later:

- Scala 3
- Apache Spark
- Apache Arrow / Parquet ecosystem

Scala is an implementation option, not part of the domain model.
