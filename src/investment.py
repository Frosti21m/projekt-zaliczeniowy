class Investment:
    def __init__(self, principal: float, annual_rate: float, years: float):
        if principal < 0:
            raise ValueError("Principal cannot be negative.")
        if annual_rate < 0:
            raise ValueError("Annual rate cannot be negative.")
        if years < 0:
            raise ValueError("Years cannot be negative.")

        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years

    def calculate_simple_interest(self) -> float:
        rate_decimal = self.annual_rate / 100
        future_value = self.principal * (1 + rate_decimal * self.years)
        return round(future_value, 2)

    def calculate_compound_interest(self) -> float:
        rate_decimal = self.annual_rate / 100
        future_value = self.principal * ((1 + rate_decimal) ** self.years)
        return round(future_value, 2)