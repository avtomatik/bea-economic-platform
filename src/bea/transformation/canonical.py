from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CanonicalPeriod:
    period_key: str
    frequency: str
    year: int
    quarter: int | None = None
    month: int | None = None


def canonicalize_period(period: str) -> CanonicalPeriod:
    if len(period) == 4 and period.isdigit():
        return CanonicalPeriod(period, "annual", int(period))
    if (
        len(period) == 6
        and period[4] == "Q"
        and period[:4].isdigit()
        and period[5].isdigit()
    ):
        quarter = int(period[5])
        if quarter not in range(1, 5):
            raise ValueError(f"Invalid quarter period: {period}")
        return CanonicalPeriod(
            period, "quarterly", int(period[:4]), quarter=quarter
        )
    if (
        len(period) == 7
        and period[4] == "M"
        and period[:4].isdigit()
        and period[5:].isdigit()
    ):
        month = int(period[5:])
        if month not in range(1, 13):
            raise ValueError(f"Invalid month period: {period}")
        return CanonicalPeriod(period, "monthly", int(period[:4]), month=month)
    raise ValueError(f"Unsupported economic period: {period}")
