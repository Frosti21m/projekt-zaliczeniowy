def get_positive_float(prompt: str, allow_zero: bool = False) -> float:
    while True:
        user_input = input(prompt)

        try:
            value = float(user_input)

            if allow_zero:
                if value < 0:
                    print("Value cannot be negative.")
                else:
                    return value
            else:
                if value <= 0:
                    print("Value must be greater than 0.")
                else:
                    return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_positive_int(prompt: str, allow_zero: bool = False) -> int:
    while True:
        user_input = input(prompt)

        try:
            value = int(user_input)

            if allow_zero:
                if value < 0:
                    print("Value cannot be negative.")
                else:
                    return value
            else:
                if value <= 0:
                    print("Value must be greater than 0.")
                else:
                    return value

        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_non_empty_string(prompt: str) -> str:
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Value cannot be empty.")
        else:
            return value