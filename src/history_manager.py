from datetime import datetime


class HistoryManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_operation(self, operation_type: str, input_data: str, result: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {operation_type} | {input_data} | Result: {result}\n"

        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(line)

    def read_history(self) -> list:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            return []