import json
import pytest

from src.currency_converter import CurrencyConverter


def test_add_rate():
    converter = CurrencyConverter()
    converter.add_rate("USD", 1.0)
    assert converter.rates["USD"] == 1.0


def test_add_rate_invalid_value():
    converter = CurrencyConverter()
    with pytest.raises(ValueError):
        converter.add_rate("USD", 0)


def test_convert_currency():
    converter = CurrencyConverter()
    converter.add_rate("USD", 1.0)
    converter.add_rate("PLN", 4.0)

    result = converter.convert(100, "USD", "PLN")
    assert result == 400.00


def test_convert_same_currency():
    converter = CurrencyConverter()
    converter.add_rate("USD", 1.0)

    result = converter.convert(100, "USD", "USD")
    assert result == 100.00


def test_convert_negative_amount():
    converter = CurrencyConverter()
    converter.add_rate("USD", 1.0)
    converter.add_rate("PLN", 4.0)

    with pytest.raises(ValueError):
        converter.convert(-50, "USD", "PLN")


def test_unknown_from_currency():
    converter = CurrencyConverter()
    converter.add_rate("USD", 1.0)

    with pytest.raises(ValueError):
        converter.convert(100, "EUR", "USD")


def test_unknown_to_currency():
    converter = CurrencyConverter()
    converter.add_rate("USD", 1.0)

    with pytest.raises(ValueError):
        converter.convert(100, "USD", "EUR")


def test_load_rates_from_file(tmp_path):
    test_file = tmp_path / "rates.json"
    data = {
        "USD": 1.0,
        "EUR": 0.92,
        "PLN": 4.0
    }

    with open(test_file, "w", encoding="utf-8") as file:
        json.dump(data, file)

    converter = CurrencyConverter()
    converter.load_rates_from_file(str(test_file))

    assert converter.rates["USD"] == 1.0
    assert converter.rates["EUR"] == 0.92
    assert converter.rates["PLN"] == 4.0


def test_load_rates_from_invalid_json(tmp_path):
    test_file = tmp_path / "bad_rates.json"

    with open(test_file, "w", encoding="utf-8") as file:
        file.write("not a json file")

    converter = CurrencyConverter()

    with pytest.raises(ValueError):
        converter.load_rates_from_file(str(test_file))