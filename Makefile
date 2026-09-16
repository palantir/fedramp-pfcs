PYTHON ?= python3
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
DEPENDENCIES_STAMP := $(VENV)/.requirements-dev.stamp

.PHONY: setup readme check-readme test verify

$(VENV_PYTHON):
	$(PYTHON) -m venv $(VENV)

$(DEPENDENCIES_STAMP): requirements-dev.txt $(VENV_PYTHON)
	$(VENV_PYTHON) -m pip install --requirement requirements-dev.txt
	touch $(DEPENDENCIES_STAMP)

setup: $(DEPENDENCIES_STAMP)

readme: $(DEPENDENCIES_STAMP)
	$(VENV_PYTHON) scripts/update_readme.py

check-readme: $(DEPENDENCIES_STAMP)
	$(VENV_PYTHON) scripts/update_readme.py --check

test: $(DEPENDENCIES_STAMP)
	$(VENV_PYTHON) -m pytest -q

verify: $(DEPENDENCIES_STAMP)
	$(VENV_PYTHON) scripts/validate_json.py
	$(VENV_PYTHON) scripts/update_readme.py --check
	$(VENV_PYTHON) -m pytest -q
