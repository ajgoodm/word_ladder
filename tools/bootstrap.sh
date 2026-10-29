#!/usr/bin/env bash
# Set up a development environment: install all dependencies (including dev)
# with uv and install the pre-commit git hooks.
set -euo pipefail

# Run from the repository root, wherever the script is called from.
cd "$(dirname "$0")/.."

if ! command -v uv >/dev/null 2>&1; then
    echo "uv is not installed. See https://docs.astral.sh/uv/getting-started/installation/" >&2
    exit 1
fi

echo "Installing dependencies..."
uv sync

echo "Installing pre-commit hooks..."
uv run pre-commit install

echo "Done. Run the CLI with: uv run word-ladder --help"
