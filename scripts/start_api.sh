#!/usr/bin/env bash
set -euo pipefail
REPO="/root/.openclaw/workspace/tmp/XHS-Downloader"
cd "$REPO"
if command -v uv >/dev/null 2>&1 && [ -f uv.lock ]; then
  exec uv run main.py api
elif [ -x .venv/bin/python ]; then
  exec .venv/bin/python main.py api
else
  exec python3 main.py api
fi
