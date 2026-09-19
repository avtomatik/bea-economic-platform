# Extracted archaeology from the legacy repository

The old scripts contained three kinds of material.

## Preserved domain knowledge

- BEA dataset families include NIPA and Fixed Assets.
- Historical release ZIP archives are meaningful source vintages.
- Series codes such as `K160021`, `K10070`, and `K16049` were used while exploring Fixed Assets/NIPA mappings.
- Spreadsheet geometry is frequency-dependent.
- Source metadata and sheet-level provenance matter.
- The existing pipeline already performs wide-to-long observation extraction.

## Deliberately removed

- ad-hoc `SeriesID(...)` probes
- one-off commented series substitutions
- network access hidden inside an enum
- experimental FRED references
- abandoned `src/main.py` research code
- hard-coded "try these IDs" logic

## Architectural conclusion

The useful output of the old code is a domain model and a parser contract. The old experimental entry points themselves are not application assets.
