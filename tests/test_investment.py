import pytest

from src.investment import Investment


def test_calculate_simple_interest():
    investment = Investment(1000, 10, 2)
    result = investment.calculate_simple_interest()
    assert result == 1200.00


def test_calculate_compound_interest():
    investment = Investment(1000, 10, 2)
    result = investment.calculate_compound_interest()
    assert result == 1210.00


def test_negative_principal():
    with pytest.raises(ValueError):
        Investment(-1000, 10, 2)


def test_negative_annual_rate():
    with pytest.raises(ValueError):
        Investment(1000, -10, 2)


def test_negative_years():
    with pytest.raises(ValueError):
        Investment(1000, 10, -2)


def test_zero_values():
    investment = Investment(0, 0, 0)
    assert investment.calculate_simple_interest() == 0.00
    assert investment.calculate_compound_interest() == 0.00