.PHONY: format check tests cov test_env dev_env venv clean fclean
PYTHON=/usr/bin/python3.10
VENV=.venv
PYEXEC=poetry run
DEV_ENV=set -a && . ./dev.env && set +a &&
TEST_ENV=set -a && . ./test.env && set +a &&

all: test

format:
	# $(PYTHON) -m ruff check --select I --fix .
	# $(PYTHON) -m isort .
	$(PYTHON) -m ruff format .

check:
ifneq ("", "$(wildcard .flake8)")
	$(PYTHON) -m flake8 .
else
	$(PYTHON) -m ruff check
endif

tests:
	$(TEST_ENV) $(VENV)/bin/pytest -vW ignore::DeprecationWarning $(ARGS)

cov:
	$(TEST_ENV) $(VENV)/bin/pytest -W ignore::DeprecationWarning  --cov --cov-report=html $(ARGS)
	open htmlcov/index.html

venv:
	poetry env use $(PYTHON)
	poetry install


clean:
	rm -rf htmlcov .coverage __pycache__ .pytest_cache .ruff_cache

fclean: clean
	rm -rf *.log *.log.[0-9]*

run:
	uvicorn main:app --reload --port 8000
