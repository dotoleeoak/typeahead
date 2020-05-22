PYTHON = python3
PIP = pip3

PROJ = typeahead
VENV_PATH = $$HOME/.virtualenvs/${PROJ}

SHELL := /bin/bash

all: clean test server

.PHONY: all setup requirements test server clean

setup:
	( \
		$(PIP) install virtualenvwrapper; \
		export WORKON_HOME=$$HOME/.virtualenvs; \
		export VIRTUALENVWRAPPER_PYTHON=/usr/bin/$(PYTHON); \
		source $$HOME/.local/bin/virtualenvwrapper.sh; \
		mkvirtualenv $(PROJ); \
	)

requirements:
	$(PIP) install -r requirements.txt

test:
	pytest test.py 

server:
	$(PYTHON) app.py

clean:
	rm -f index.txt word-count.txt 
	rm -rf __pycache__ .pytest_cache
