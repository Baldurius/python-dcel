#!/bin/sh

SCRIPT_DIR=$(dirname "$0")
PROJECT_DIR=$SCRIPT_DIR
TEST_DIR="$PROJECT_DIR/tests"

echo "Running pycodestyle"
python3 -m pycodestyle $PROJECT_DIR

echo "Running mypy"
python3 -m mypy \
    $PROJECT_DIR \
    --disallow-untyped-calls \
    --disallow-incomplete-defs \
    --disallow-untyped-decorators \
    --disallow-untyped-defs \
    --warn-redundant-casts \
    --warn-unused-ignores \
    --no-warn-no-return \
    --warn-return-any \
    --warn-unreachable

echo "Running tests"
python3 -m pytest \
    --cov=dcel \
    --cov-report html \
    --cov-report term \
    $TEST_DIR
