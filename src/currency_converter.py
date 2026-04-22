import json


class CurrencyConverter:
    def __init__(self):
        self.rates = {}

    def add_rate(self, currency_code: str, rate: float):
        currency_code = currency_code.upper()

        if rate <= 0:
            raise ValueError("Exchange rate must be greater than 0.")

        self.rates[currency_code] = rate

    def load_rates_from_file(self, file_path: str):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("Invalid file format. JSON must contain an object.")

            for currency_code, rate in data.items():
                self.add_rate(currency_code, rate)

        except FileNotFoundError:
            raise FileNotFoundError("Rates file not found.")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in rates file.")

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        if amount < 0:
            raise ValueError("Amount cannot be negative.")

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates:
            raise ValueError(f"Unknown currency: {from_currency}")
        if to_currency not in self.rates:
            raise ValueError(f"Unknown currency: {to_currency}")

        amount_in_base = amount / self.rates[from_currency]
        converted_amount = amount_in_base * self.rates[to_currency]

        return round(converted_amount, 2)