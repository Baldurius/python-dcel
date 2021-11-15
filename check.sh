#!/bin/sh

SCRIPT_DIR=$(dirname "$0")
PROJECT_DIR=$SCRIPT_DIR
TEST_DIR="$PROJECT_DIR/tests"

echo "Running pycodestyle"
python3 -m pycodestyle $PROJECT_DIR

echo "Running mypy"
python3 -m mypy $PROJECT_DIR

echo "Running tests"
python3 -m pytest $TEST_DIR
