include .env
export


## Format all
fmt: format
format: isort black


## Check code quality
chk: check
lint: check
check: flake black_check isort_check

mypy:
	mypy core delivery card


## Sort imports
isort:
	isort core delivery card

isort_check:
	isort --check-only core delivery card


## Format code
black:
	black --config pyproject.toml core delivery card

black_check:
	black --config pyproject.toml --diff --check core delivery card


# Check pep8
flake:
	flake8 --config .flake8 core delivery card