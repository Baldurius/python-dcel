#!/bin/sh

SCRIPT_DIR=$(dirname "$0")
PROJECT_DIR=$SCRIPT_DIR

echo "Running pycodestyle"
python3 -m pycodestyle $PROJECT_DIR

echo "Running mypy"
python3 -m mypy $PROJECT_DIR
