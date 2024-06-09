import pytest
import sys

from main import main

def test_if_any_no_valid_argument_was_input(capsys, monkeypatch):
    test_args = ["main.py", "-Sumary", "--month", "Jan", "--year", "2024","--json_path", "/path/to/your/file.json"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with pytest.raises(SystemExit) as exception_info:
        main()

    captured = capsys.readouterr()

    assert exception_info.type == SystemExit
    assert exception_info.value.code == 1
    assert 'No valid argument(s) was(were) provided. Use --h for more information.' in captured.out  

def test_no_summary_argument(capsys, monkeypatch):
    test_args = ["main.py", "--month", "Jan", "--year", "2024","--json_path", "/path/to/your/file.json"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with pytest.raises(SystemExit) as exception_info:
        main()

    captured = capsys.readouterr()

    assert exception_info.type == SystemExit
    assert exception_info.value.code == 1
    assert 'No --summary argument provided. Use --h for more information.' in captured.out

def test_no_json_path_argument(capsys, monkeypatch):
    test_args = ["main.py", "--summary", "--month", "Jan", "--year", "2024"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with pytest.raises(SystemExit) as exception_info:
        main()

    captured = capsys.readouterr()

    assert exception_info.type == SystemExit
    assert exception_info.value.code == 1
    assert 'No --json_path argument provided. Use --h for more information.' in captured.out

def test_no_month_argument(capsys, monkeypatch):
    test_args = ["main.py", "--summary", "--year", "2024","--json_path", "/path/to/your/file.json"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with pytest.raises(SystemExit) as exception_info:
        main()

    captured = capsys.readouterr()

    assert exception_info.type == SystemExit
    assert exception_info.value.code == 1
    assert 'No --month argument provided. Use --h for more information.' in captured.out

@pytest.mark.parametrize("test_month_input", ["JAN", "FEV.", "Mar", "Apr.", "may", "jun.", ""])
def test_if_month_argument_input_is_valid(capsys, monkeypatch, test_month_input):
    test_args = ["main.py", "--summary", "--month", test_month_input, "--year", "2024","--json_path", "/path/to/your/file.json"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with pytest.raises(SystemExit) as exception_info:
        main()

    captured = capsys.readouterr()

    assert exception_info.type == SystemExit
    assert exception_info.value.code == 1
    assert 'The --month input provided does not exist. Use --h for more information.' in captured.out

def test_no_year_argument(capsys, monkeypatch):
    test_args = ["main.py", "--summary", "--month", "May", "--json_path", "/path/to/your/file.json"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with pytest.raises(SystemExit) as exception_info:
        main()

    captured = capsys.readouterr()

    assert exception_info.type == SystemExit
    assert exception_info.value.code == 1
    assert 'No --year argument provided. Use --h for more information.' in captured.out