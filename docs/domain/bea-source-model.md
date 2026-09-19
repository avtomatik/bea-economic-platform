# BEA source model

## Source datasets

The historical scripts demonstrate at least two BEA dataset families:

- National Income and Product Accounts (NIPA)
- Fixed Assets Accounts (FIAS / Fixed Assets)

A dataset is a stable logical source. A release is a dated publication/vintage of that dataset. A source artifact is a concrete archive, workbook, or sheet belonging to a release.

```text
Dataset
  -> Release / vintage
      -> Archive
          -> Workbook
              -> Sheet
                  -> Economic table
                      -> Series
                          -> Observation
```

## Why release/vintage is first-class

An observation is not identified only by series and period when historical BEA releases are being preserved. The same historical period can be revised in later releases.

The analytical identity therefore needs to be understood as:

```text
(series, period, release/vintage)
```

A separate "current/latest" view can collapse vintages later, but the raw historical record should not.
