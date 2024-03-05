# Makefile
# Run "make lint" to run the lint target

lint:
    pylint src
    flake8 src