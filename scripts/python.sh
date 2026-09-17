#!/bin/sh
# Run Python with this repository's dependencies, installing them when needed.
set -eu
cd "$(dirname "$0")/.."

if [ ! -x .venv/bin/python ]; then
    "${PYTHON:-python3}" -m venv .venv
fi

if [ ! -f .venv/.requirements-dev.stamp ] ||
   [ requirements-dev.txt -nt .venv/.requirements-dev.stamp ]; then
    .venv/bin/python -m pip install --requirement requirements-dev.txt
    touch .venv/.requirements-dev.stamp
fi

exec .venv/bin/python "$@"
