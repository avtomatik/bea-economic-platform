import pytest

from bea.transformation.canonical import canonicalize_period


def test_canonical_periods():
    assert canonicalize_period("1929").year == 1929
    assert canonicalize_period("2012Q1").quarter == 1
    assert canonicalize_period("2012M09").month == 9


def test_invalid_quarter_rejected():
    with pytest.raises(ValueError):
        canonicalize_period("2012Q5")


def test_invalid_month_rejected():
    with pytest.raises(ValueError):
        canonicalize_period("2012M13")
