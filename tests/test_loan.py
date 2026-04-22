import pytest

from src.loan import Loan


def test_calculate_monthly_payment():
    loan = Loan(12000, 12, 12)
    result = loan.calculate_monthly_payment()
    assert result == 1066.19


def test_calculate_monthly_payment_zero_interest():
    loan = Loan(12000, 0, 12)
    result = loan.calculate_monthly_payment()
    assert result == 1000.00


def test_generate_schedule_length():
    loan = Loan(12000, 12, 12)
    schedule = loan.generate_schedule()
    assert len(schedule) == 12


def test_last_balance_is_zero():
    loan = Loan(12000, 12, 12)
    schedule = loan.generate_schedule()
    assert schedule[-1]["balance"] == 0.0


def test_invalid_loan_amount():
    with pytest.raises(ValueError):
        Loan(0, 12, 12)


def test_negative_annual_rate():
    with pytest.raises(ValueError):
        Loan(12000, -5, 12)


def test_invalid_months():
    with pytest.raises(ValueError):
        Loan(12000, 12, 0)