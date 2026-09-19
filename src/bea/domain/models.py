from dataclasses import dataclass
from enum import StrEnum
from typing import Final


class Frequency(StrEnum):
    ANNUAL = "annual"
    QUARTERLY = "quarterly"
    MONTHLY = "monthly"


@dataclass(frozen=True, slots=True)
class SourceProvenance:
    source_archive: str
    source_file: str
    source_sheet: str


@dataclass(frozen=True, slots=True)
class TableMetadata:
    table_title: str | None
    table_note: str | None
    coverage_note: str | None
    source_agency: str | None
    published_at_raw: str | None
    file_created_at_raw: str | None


@dataclass(frozen=True, slots=True)
class EconomicObservation:
    table_title: str | None
    table_note: str | None
    coverage_note: str | None
    source_agency: str | None
    published_at_raw: str | None
    file_created_at_raw: str | None
    frequency: Frequency
    line_number: str | None
    line_description: str
    series_code: str | None
    period: str
    value: float
    source_archive: str
    source_file: str
    source_sheet: str


SUPPORTED_FREQUENCIES: Final[frozenset[Frequency]] = frozenset(Frequency)
