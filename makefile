#!/usr/bin/env make

# Change this to be your variant of the python command
# Set the env variable PYTHON to another value if needed
# PYTHON=python3 make version
PYTHON ?= python # python3 py

# Print out colored action message
MESSAGE = printf "\033[32;01m---> $(1)\033[0m\n"

all:


# ---------------------------------------------------------
# Check the current python executable.
#
version:
	@printf "Currently using executable: $(PYTHON)\n"
	which $(PYTHON)
	$(PYTHON) --version


# ---------------------------------------------------------
# Setup a venv and install packages.
#
venv:
	[ -d .venv ] || $(PYTHON) -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n"

install:
	$(PYTHON) -m pip install -r requirements.txt

installed:
	$(PYTHON) -m pip list


# ---------------------------------------------------------
# Cleanup generated and installed files.
#
clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv


# ---------------------------------------------------------
# Work with static code linters.
#
pylint:
	@$(call MESSAGE,$@)
	- $(PYTHON) -m pylint src/**/*.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint


# ---------------------------------------------------------
# Work with codestyle.
#
black:
	@$(call MESSAGE,$@)
	 $(PYTHON) -m black src/ test/

codestyle: black


# ---------------------------------------------------------
# Work with unit test and code coverage.
#
unittest:
	@$(call MESSAGE,$@)
	$(PYTHON) -m unittest discover -s src/game -p "test_*.py"

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest discover -s src/game -p "test_*.py"
	coverage html
	coverage report -m

test: coverage


# ---------------------------------------------------------
# Work with generating documentation.
#

pdoc:
	@$(call MESSAGE,$@)
	pdoc --force --html --output-dir doc/api src/game/*.py

pyreverse:
	@$(call MESSAGE,$@)
	pyreverse src/game
	dot -Tpng classes.dot -o doc/uml/classes.png
	dot -Tpng packages.dot -o doc/uml/packages.png

doc: pdoc

uml: pyreverse

# ---------------------------------------------------------
# Calculate software metrics for your project.
#
radon-cc:
	@$(call MESSAGE,$@)
	radon cc --show-complexity --average src

radon-mi:
	@$(call MESSAGE,$@)
	radon mi --show src

radon-raw:
	@$(call MESSAGE,$@)
	radon raw src

radon-hal:
	@$(call MESSAGE,$@)
	radon hal src

cohesion:
	@$(call MESSAGE,$@)
	cohesion --directory src

metrics: radon-cc radon-mi radon-raw radon-hal cohesion



# ---------------------------------------------------------
# Find security issues in your project.
#
bandit:
	@$(call MESSAGE,$@)
	bandit --recursive src


# ---------------------------------------------------------
# Run game
#
.PHONY: run

run:
	python3 src/game/game.py 
