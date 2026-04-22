from src.currency_converter import CurrencyConverter
from src.history_manager import HistoryManager
from src.investment import Investment
from src.loan import Loan
from src.utils import get_non_empty_string, get_positive_float, get_positive_int


class Menu:
    def __init__(self):
        self.history_manager = HistoryManager("data/history.txt")
        self.currency_converter = CurrencyConverter()

        try:
            self.currency_converter.load_rates_from_file("data/exchange_rates.json")
        except (FileNotFoundError, ValueError):
            pass

    def show_main_menu(self):
        while True:
            print("\n=== Financial Calculator ===")
            print("1. Investment calculator")
            print("2. Loan calculator")
            print("3. Currency converter")
            print("4. Show history")
            print("5. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.investment_menu()
            elif choice == "2":
                self.loan_menu()
            elif choice == "3":
                self.currency_converter_menu()
            elif choice == "4":
                self.show_history()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def investment_menu(self):
        print("\n=== Investment Calculator ===")
        principal = get_positive_float("Enter principal amount: ", allow_zero=True)
        annual_rate = get_positive_float("Enter annual interest rate (%): ", allow_zero=True)
        years = get_positive_float("Enter number of years: ", allow_zero=True)

        try:
            investment = Investment(principal, annual_rate, years)
        except ValueError as error:
            print(f"Error: {error}")
            return

        print("1. Simple interest")
        print("2. Compound interest")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            result = investment.calculate_simple_interest()
            print(f"Future value (simple interest): {result}")
            self.history_manager.save_operation(
                "Investment - Simple Interest",
                f"principal={principal}, rate={annual_rate}, years={years}",
                str(result)
            )
        elif choice == "2":
            result = investment.calculate_compound_interest()
            print(f"Future value (compound interest): {result}")
            self.history_manager.save_operation(
                "Investment - Compound Interest",
                f"principal={principal}, rate={annual_rate}, years={years}",
                str(result)
            )
        else:
            print("Invalid option.")

    def loan_menu(self):
        print("\n=== Loan Calculator ===")
        loan_amount = get_positive_float("Enter loan amount: ")
        annual_rate = get_positive_float("Enter annual interest rate (%): ", allow_zero=True)
        months = get_positive_int("Enter number of months: ")

        try:
            loan = Loan(loan_amount, annual_rate, months)
        except ValueError as error:
            print(f"Error: {error}")
            return

        print("1. Monthly payment")
        print("2. Repayment schedule")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            result = loan.calculate_monthly_payment()
            print(f"Monthly payment: {result}")
            self.history_manager.save_operation(
                "Loan - Monthly Payment",
                f"loan_amount={loan_amount}, rate={annual_rate}, months={months}",
                str(result)
            )
        elif choice == "2":
            schedule = loan.generate_schedule()
            print("\nRepayment schedule:")
            for row in schedule:
                print(
                    f"Month: {row['month']}, "
                    f"Payment: {row['payment']}, "
                    f"Interest: {row['interest']}, "
                    f"Principal: {row['principal']}, "
                    f"Balance: {row['balance']}"
                )

            self.history_manager.save_operation(
                "Loan - Repayment Schedule",
                f"loan_amount={loan_amount}, rate={annual_rate}, months={months}",
                "Schedule generated"
            )
        else:
            print("Invalid option.")

    def currency_converter_menu(self):
        print("\n=== Currency Converter ===")
        print("1. Convert currency")
        print("2. Add exchange rate manually")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            amount = get_positive_float("Enter amount: ", allow_zero=True)
            from_currency = get_non_empty_string("From currency: ").upper()
            to_currency = get_non_empty_string("To currency: ").upper()

            try:
                result = self.currency_converter.convert(amount, from_currency, to_currency)
                print(f"Converted amount: {result}")

                self.history_manager.save_operation(
                    "Currency Conversion",
                    f"amount={amount}, from={from_currency}, to={to_currency}",
                    str(result)
                )
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            currency_code = get_non_empty_string("Enter currency code: ").upper()
            rate = get_positive_float("Enter exchange rate: ")

            try:
                self.currency_converter.add_rate(currency_code, rate)
                print(f"Rate for {currency_code} added successfully.")

                self.history_manager.save_operation(
                    "Currency Rate Added",
                    f"currency={currency_code}, rate={rate}",
                    "Success"
                )
            except ValueError as error:
                print(f"Error: {error}")
        else:
            print("Invalid option.")

    def show_history(self):
        print("\n=== History ===")
        history = self.history_manager.read_history()

        if not history:
            print("No history available.")
            return

        for line in history:
            print(line)