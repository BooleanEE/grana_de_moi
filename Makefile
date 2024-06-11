save:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

run:
	python main.py --summary --month January --year 2024 --json_path ./data/mon_finance.json
