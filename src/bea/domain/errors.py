class BeaIngestionError(Exception):
    """Base class for expected BEA ingestion errors."""


class UnsupportedSpreadsheetGeometry(BeaIngestionError):
    """Raised when a workbook/sheet does not match the known source geometry."""
