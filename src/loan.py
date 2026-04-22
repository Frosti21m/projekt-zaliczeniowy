class Loan:
    def __init__(self, loan_amount: float, annual_rate: float, months: int):
        if loan_amount <= 0:
            raise ValueError("Loan amount must be greater than 0.")
        if annual_rate < 0:
            raise ValueError("Annual rate cannot be negative.")
        if months <= 0:
            raise ValueError("Number of months must be greater than 0.")

        self.loan_amount = loan_amount
        self.annual_rate = annual_rate
        self.months = months

    def calculate_monthly_payment(self) -> float:
        if self.annual_rate == 0:
            monthly_payment = self.loan_amount / self.months
            return round(monthly_payment, 2)

        monthly_rate = (self.annual_rate / 100) / 12
        numerator = self.loan_amount * monthly_rate * (1 + monthly_rate) ** self.months
        denominator = (1 + monthly_rate) ** self.months - 1
        monthly_payment = numerator / denominator

        return round(monthly_payment, 2)

    def generate_schedule(self) -> list:
        schedule = []
        remaining_balance = self.loan_amount
        monthly_payment = self.calculate_monthly_payment()

        if self.annual_rate == 0:
            for month_number in range(1, self.months + 1):
                interest_part = 0.0
                capital_part = monthly_payment

                if month_number == self.months:
                    capital_part = round(remaining_balance, 2)
                    monthly_payment_for_row = round(capital_part + interest_part, 2)
                else:
                    monthly_payment_for_row = monthly_payment

                remaining_balance = round(remaining_balance - capital_part, 2)
                if remaining_balance < 0:
                    remaining_balance = 0.0

                schedule.append({
                    "month": month_number,
                    "payment": monthly_payment_for_row,
                    "interest": round(interest_part, 2),
                    "principal": round(capital_part, 2),
                    "balance": round(remaining_balance, 2)
                })

            return schedule

        monthly_rate = (self.annual_rate / 100) / 12

        for month_number in range(1, self.months + 1):
            interest_part = round(remaining_balance * monthly_rate, 2)
            capital_part = round(monthly_payment - interest_part, 2)

            if month_number == self.months:
                capital_part = round(remaining_balance, 2)
                monthly_payment_for_row = round(capital_part + interest_part, 2)
            else:
                monthly_payment_for_row = monthly_payment

            remaining_balance = round(remaining_balance - capital_part, 2)
            if remaining_balance < 0:
                remaining_balance = 0.0

            schedule.append({
                "month": month_number,
                "payment": monthly_payment_for_row,
                "interest": round(interest_part, 2),
                "principal": round(capital_part, 2),
                "balance": round(remaining_balance, 2)
            })

        return schedule