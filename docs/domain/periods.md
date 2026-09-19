# Economic periods

The legacy spreadsheets encode periods in a frequency-dependent geometry:

- annual: `YYYY`
- quarterly: `YYYYQn`
- monthly: `YYYYMnn`

The raw layer should preserve the source representation. The canonical layer should expose typed period components (`year`, `quarter`, `month`) plus a canonical period key.

The parser is intentionally separate from analytical period semantics: parsing answers "what did the spreadsheet contain?" while canonicalization answers "how should the platform represent it?".
