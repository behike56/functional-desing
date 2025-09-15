.PHONY: run test lint format

run:
	poetry run python src/functional_py/main.py

test:
	poetry run pytest

lint:
	poetry run ruff check .

format:
	poetry run ruff format .
