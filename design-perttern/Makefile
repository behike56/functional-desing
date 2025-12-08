POETRY ?= poetry
PY ?= $(POETRY) run python

.PHONY: help install run check clean shell

.DEFAULT_GOAL := help

help:
	@echo "Available targets:"
	@echo "  install  - Resolve and install dependencies with Poetry"
	@echo "  run      - Run adapter demo (JSON + XML)"
	@echo "  check    - Verify bs4/lxml availability"
	@echo "  clean    - Remove caches (__pycache__, .pytest_cache, etc.)"
	@echo "  shell    - Enter Poetry virtual environment shell"

install:
	$(POETRY) lock -n
	$(POETRY) install -n

run:
	$(PY) src/design_perttern/adapter_perttern/main.py

check:
	$(PY) -c "import bs4, lxml; print('beautifulsoup4/lxml OK')"

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	rm -rf .pytest_cache .ruff_cache .mypy_cache

shell:
	$(POETRY) shell

