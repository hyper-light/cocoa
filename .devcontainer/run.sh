#!/usr/bin/env bash
git config --global --add safe.directory /workspace
if [[ ! -d /workspace/.venv ]]; then
    uv venv
fi

. /workspace/.venv/bin/activate && \
uv pip install -r requirements.txt && \
uv pip install -e .
