install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

check: lint test

.PHONY: install lint test test-coverage check
