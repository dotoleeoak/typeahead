PYTHON = python3
PIP = pip3

PROJ = typeahead
VENV_PATH = $$HOME/.virtualenvs/${PROJ}
SERVER_SETTING = config/config.py

all: clean test server

.PHONY: all setup requirements test server clean

setup:
	$(PYTHON) -m venv $(VENV_PATH) --clear

requirements:
	$(PIP) install -r requirements.txt

test:
	rm -r typeahead_index/*
	$(PYTHON) -m pytest

server:
	FLASK_APP=$(PROJ) TYPEAHEAD_SETTINGS=$(SERVER_SETTING) $(PYTHON) -m flask run -p 5000

clean:
	rm -f index.txt word-count.txt 
	rm -rf ./__pycache__ */__pycache__ .pytest_cache
