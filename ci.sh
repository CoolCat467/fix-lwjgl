#!/bin/bash

set -ex -o pipefail

# Log some general info about the environment
echo "::group::Environment"
uname -a
env | sort
PROJECT='fix_lwjgl'
echo "::endgroup::"


################################################################
# We have a Python environment!
################################################################

echo "::group::Versions"
python -c "import sys, struct; print('python:', sys.version); print('version_info:', sys.version_info); print('bits:', struct.calcsize('P') * 8)"
echo "::endgroup::"

echo "::group::Install dependencies"
python -m pip install -U pip tomli
python -m pip --version
UV_VERSION=$(python -c 'import tomli; from pathlib import Path; print({p["name"]:p for p in tomli.loads(Path("uv.lock").read_text())["package"]}["uv"]["version"])')
python -m pip install uv==$UV_VERSION
python -m uv --version

UV_VENV_SEED="pip"
python -m uv venv --seed --allow-existing

# Determine the platform and activate the virtual environment accordingly
case "$OSTYPE" in
  linux-gnu*|linux-musl*|darwin*)
    source .venv/bin/activate
    ;;
  cygwin*|msys*)
    source .venv/Scripts/activate
    ;;
  *)
    echo "::error:: Unknown OS. Please add an activation method for '$OSTYPE'."
    exit 1
    ;;
esac

# Install uv in virtual environment
python -m pip install uv==$UV_VERSION

if [ "$CHECK_FORMATTING" = "1" ]; then
    python -m uv sync --locked --extra tests --extra tools
    echo "::endgroup::"
    source check.sh
else
    # Actual tests
    # expands to 0 != 1 if NO_TEST_REQUIREMENTS is not set, if set the `-0` has no effect
    # https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02
    if [ "${NO_TEST_REQUIREMENTS-0}" == 1 ]; then
        python -m uv sync --locked --extra tests
        #"--skip-optional-imports"
    else
        python -m uv sync --locked --extra tests --extra tools
    fi

    echo "::endgroup::"

    echo "::group::Setup for tests"

    echo "::endgroup::"
    echo "::group:: Run Tests"
    if pytest -ra --junitxml=test-results.xml tests --verbose --durations=10; then
        PASSED=true
    else
        PASSED=false
    fi
    echo "::endgroup::"

    $PASSED
fi
