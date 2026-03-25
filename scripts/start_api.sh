#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPO="${XHS_DOWNLOADER_DIR:-$ROOT_DIR/vendor/XHS-Downloader}"

if [ ! -d "$REPO" ]; then
  echo "[xhs-skill] Upstream repo not found at $REPO" >&2
  echo "[xhs-skill] Run: bash scripts/install.sh" >&2
  exit 1
fi

cd "$REPO"
if command -v uv >/dev/null 2>&1 && [ -f uv.lock ]; then
  exec uv run main.py api
elif [ -x .venv/bin/python ]; then
  exec .venv/bin/python main.py api
else
  exec python3 main.py api
fi