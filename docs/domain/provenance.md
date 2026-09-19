# Provenance

Every extracted observation must remain traceable to the source artifact that produced it.

Minimum provenance chain:

```text
source_archive
source_file
source_sheet
```

Recommended future extension:

```text
source_dataset
release_id
archive_sha256
source_file_sha256
parser_version
ingested_at
```

Provenance is intentionally modeled separately from business/economic attributes. It should be possible to audit an analytical value back to its original workbook and sheet without copying all provenance strings into every dimensional table.
