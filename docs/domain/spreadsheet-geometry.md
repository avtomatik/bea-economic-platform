# Spreadsheet geometry contract

The current BEA historical Excel family is semi-structured. The parser relies on explicit geometry discovered during reverse engineering.

Current reference rules:

```text
LINE_ROW          = 7
DESCRIPTION_COL   = 1
SERIES_CODE_COL   = 2
VALUE_START_COL   = 3

annual data starts at row 8
quarterly data starts at row 9
monthly data starts at row 9
```

Metadata is currently found in the first six rows:

```text
0 table title
1 table note
2 coverage note
3 source agency
4 publication timestamp (raw)
5 file created timestamp (raw)
```

Frequency is inferred from the coverage note:

```text
Annual data...     -> annual
Quarterly data...  -> quarterly
Monthly data...    -> monthly
```

Period headers are read from `LINE_ROW` and, for subannual frequencies, `LINE_ROW + 1`.

A blank line description terminates the data table.

These are source-family parsing rules, not universal BEA truths. They are therefore isolated in the ingestion package and covered by unit tests.
