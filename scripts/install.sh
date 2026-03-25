#!/usr/bin/env bash
set -euo pipefail
REPO="/root/.openclaw/workspace/tmp/XHS-Downloader"
cd "$REPO"
if command -v uv >/dev/null 2>&1; then
  uv sync --no-dev
else
  python3 -m venv .venv
  . .venv/bin/activate
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
fi
