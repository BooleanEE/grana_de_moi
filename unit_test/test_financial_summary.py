import os
import pytest

from financial_summary import FinancialSummary

@pytest.fixture(scope='session')
def json_path_for_financial_summary_testing():
    unit_test_directory_path = os.path.dirname(__file__)
    json_path_test = os.path.join(unit_test_directory_path, "test_mon_finance.json") 
    return json_path_test

@pytest.fixture
def invalid_json_file(tmp_path):
    file_path = tmp_path / "invalid_file.json"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("{invalid_json: }")
    return str(file_path)

def test_json_path_does_not_exists():
    with pytest.raises(FileNotFoundError):
        FinancialSummary("test_mon_finance_not_exist.json", "November", "2023")   

def test_json_path_exists(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path_for_financial_summary_testing, "November", "2023")
    assert financial_summary.json_exists is True

def test_invalid_json_file(invalid_json_file):
    with pytest.raises(ValueError):
        FinancialSummary(json_path=invalid_json_file, month="January", year="2023")

def test_valid_json_file(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path=json_path_for_financial_summary_testing, month="January", year="2023")
    assert financial_summary.json_valid is True


def test_if_year_does_not_exist_in_the_provided_json(json_path_for_financial_summary_testing):
    with pytest.raises(KeyError, match="The input year does not exist in the provided JSON file."):
        FinancialSummary(json_path=json_path_for_financial_summary_testing, month="January", year="2025")

def test_if_month_for_the_selected_year_does_not_exists_in_the_provided_json(json_path_for_financial_summary_testing):
    with pytest.raises(KeyError, match="The input month for the input year does not exist in the provided JSON file."):
        FinancialSummary(json_path=json_path_for_financial_summary_testing, month='December', year="2024")

def test_if_income_is_empty_for_the_selected_year_and_month(json_path_for_financial_summary_testing):
    with pytest.raises(ValueError, match="The /'Income/' is empty for the provided JSON file for the year and month selected. Check if your JSON file is correct."):
        FinancialSummary(json_path=json_path_for_financial_summary_testing, month="June", year="2024")

def test_if_expense_is_empty_for_the_selected_year_and_month(json_path_for_financial_summary_testing):
    with pytest.raises(ValueError, match="The /'Expenses/' is empty for the provided JSON file for the year and month selected. Check if your JSON file is correct."):
        FinancialSummary(json_path=json_path_for_financial_summary_testing, month="July", year="2024")

def test_income_total_calculation(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path=json_path_for_financial_summary_testing, month="March", year="2024")
    total_income_value_march_2024 = 5400.00
    assert total_income_value_march_2024 == financial_summary.total_income

def test_expense_total_calculation(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path=json_path_for_financial_summary_testing, month="April", year="2023")
    total_expense_value_april_2023 = 4300.00
    assert total_expense_value_april_2023 == financial_summary.total_expenses

def test_income_representation_by_income_type(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path=json_path_for_financial_summary_testing, month="March", year="2024")
    financial_income_representation_march_2024 = {'Salary': 0.9444,
                                                  'Investments': 0.0556}
    assert financial_income_representation_march_2024 == financial_summary.income_representation_by_type

def test_expense_representation_by_expense_type(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path=json_path_for_financial_summary_testing, month="March", year="2024")
    financial_expenses_representation_march_2024 = {'Clothing': 0.0455, 
                                                    'Debt': 0.0594, 
                                                    'Education': 0.101, 
                                                    'Entertainment': 0.0396, 
                                                    'Food': 0.1347, 
                                                    'Gifts': 0.0297, 
                                                    'Housing': 0.2, 
                                                    'Insurance': 0.0416, 
                                                    'Medical': 0.0416, 
                                                    'Personal': 0.0436, 
                                                    'Savings': 0.0851, 
                                                    'Supplies': 0.0396, 
                                                    'Transportation': 0.0792, 
                                                    'Utilities': 0.0594
                                                    }
                                                  
    assert financial_expenses_representation_march_2024 == financial_summary.expenses_representation_by_type

def test_if_the_most_significant_income_is_correctly_matched(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path=json_path_for_financial_summary_testing, month="March", year="2024")
    most_significant_income_march_2024 = 'Salary'
    assert most_significant_income_march_2024 == financial_summary.most_significant_income

def test_if_the_most_significant_expense_is_correctly_matched(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path=json_path_for_financial_summary_testing, month="March", year="2024")
    most_significant_expense_march_2024 = 'Housing'
    assert most_significant_expense_march_2024 == financial_summary.most_significant_expense

def test_the_financial_balance_calculation_correctness(json_path_for_financial_summary_testing):
    financial_summary = FinancialSummary(json_path=json_path_for_financial_summary_testing, month="March", year="2024")
    financial_balance_march_2024 = 350
    assert financial_balance_march_2024 == financial_summary.balance
