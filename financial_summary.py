import os
import json

class FinancialSummary:
    def __init__(self, json_path: str, month: str, year: str):
        self.finance_json_loaded_file = None
        self.json_exists = False
        self.json_path = json_path
        self.json_valid = False
        self.month = month
        self.year = year
        self.total_income = float(0)
        self.total_expenses = float(0)
        self.income_representation_by_type = {}
        self.expenses_representation_by_type = {}
        self.most_significant_income = None
        self.most_significant_expense = None
        self.balance = None

        self.check_json_integrity()
        self.check_if_year_exists_in_the_provided_json_file()
        self.check_if_year_month_exists_in_the_provided_json_file()
        self.check_if_income_is_empty_for_the_current_year_and_month_input_in_the_provided_json_file()
        self.check_if_expense_is_empty_for_the_current_year_and_month_input_in_the_provided_json_file()

        self.calculate_total_income_for_selected_year_and_month()
        self.calculate_total_expenses_for_selected_year_and_month()
        self.evaluate_income_representation_by_type_for_selected_year_and_month()
        self.evaluate_expenses_representation_by_type_for_selected_year_and_month()
        self.get_most_significant_income_for_selected_year_and_month()
        self.get_most_significant_expense_for_selected_year_and_month()
        self.calculate_financial_balance_for_selected_year_and_month()
        self.generate_financial_summary()

    def check_json_integrity(self) -> None:
        self.does_the_provided_json_path_exist()
        self.is_the_provided_json_file_valid()
        if not self.json_exists:
            raise FileNotFoundError(f"The file at path {self.json_path} does not exist.")
        if not self.json_valid:
            raise ValueError(f"The file at path {self.json_path} is not a valid JSON file.")

    def does_the_provided_json_path_exist(self) -> None:
        self.json_exists = os.path.exists(self.json_path)

    def is_the_provided_json_file_valid(self) -> None:
        if self.json_exists:
            try:
                with open(self.json_path, 'r', encoding='utf-8') as file:
                    self.finance_json_loaded_file = json.load(file)
                    self.json_valid = True
            except (json.JSONDecodeError, IOError) as exception_info:
                print(exception_info)
                self.json_valid = False
        else:
            self.json_valid = False

    def check_if_year_exists_in_the_provided_json_file(self) -> None:
        if self.year not in self.finance_json_loaded_file:
            raise KeyError("The input year does not exist in the provided JSON file.")

    def check_if_year_month_exists_in_the_provided_json_file(self) -> None:
        if self.month not in self.finance_json_loaded_file[self.year]:
            raise KeyError("The input month for the input year does not exist in the provided JSON file.")
        
    def check_if_income_is_empty_for_the_current_year_and_month_input_in_the_provided_json_file(self) -> None:
        if not self.finance_json_loaded_file[self.year][self.month]['Income']:
            raise ValueError("The /'Income/' is empty for the provided JSON file for the year and month selected. Check if your JSON file is correct.")

    def check_if_expense_is_empty_for_the_current_year_and_month_input_in_the_provided_json_file(self) -> None:
        if not self.finance_json_loaded_file[self.year][self.month]['Expenses']:
            raise ValueError("The /'Expenses/' is empty for the provided JSON file for the year and month selected. Check if your JSON file is correct.")
        
    def calculate_total_income_for_selected_year_and_month(self):
        for incomes in self.finance_json_loaded_file[self.year][self.month]['Income']:
            self.total_income += self.finance_json_loaded_file[self.year][self.month]['Income'][incomes]

    def calculate_total_expenses_for_selected_year_and_month(self):
        for expenses in self.finance_json_loaded_file[self.year][self.month]['Expenses']:
            self.total_expenses += self.finance_json_loaded_file[self.year][self.month]['Expenses'][expenses]

    def evaluate_income_representation_by_type_for_selected_year_and_month(self):
        for incomes in self.finance_json_loaded_file[self.year][self.month]['Income']:
            current_income_value = self.finance_json_loaded_file[self.year][self.month]['Income'][incomes]
            representation_of_current_income = round(current_income_value/self.total_income, 4)
            self.income_representation_by_type.update({incomes: f"{representation_of_current_income:.4f}"})

    def evaluate_expenses_representation_by_type_for_selected_year_and_month(self):
        for expenses in self.finance_json_loaded_file[self.year][self.month]['Expenses']:
            current_expense_value = self.finance_json_loaded_file[self.year][self.month]['Expenses'][expenses]
            representation_of_current_expense = round(current_expense_value/self.total_expenses, 4)
            self.expenses_representation_by_type.update({expenses: f"{representation_of_current_expense:.4f}"})

    def get_most_significant_income_for_selected_year_and_month(self):
        self.most_significant_income = max(self.income_representation_by_type, key=self.income_representation_by_type.get)

    def get_most_significant_expense_for_selected_year_and_month(self):
        self.most_significant_expense = max(self.expenses_representation_by_type, key=self.expenses_representation_by_type.get)

    def calculate_financial_balance_for_selected_year_and_month(self):
        self.balance = self.total_income - self.total_expenses

    def generate_financial_summary(self):
        print(f"{self.month} {self.year} Summary:")
        print("-" * 30)
        print(f"Total Income: R$ {self.total_income:.2f}")
        print(f"Total Expenses: R$ {self.total_expenses:.2f}")
        print(f"Balance: R$ {self.balance:.2f}")
        print(f"Most Significant Income: {self.most_significant_income} ({self.income_representation_by_type[self.most_significant_income]})")
        print(f"Most Significant Expense: {self.most_significant_expense} ({self.expenses_representation_by_type[self.most_significant_expense]})")
        print("-" * 30)
