#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
UPSTREAM_DIR="${XHS_DOWNLOADER_DIR:-$ROOT_DIR/vendor/XHS-Downloader}"
UPSTREAM_REPO="${XHS_DOWNLOADER_REPO:-https://github.com/JoeanAmier/XHS-Downloader.git}"

mkdir -p "$(dirname "$UPSTREAM_DIR")"

if [ ! -d "$UPSTREAM_DIR/.git" ]; then
  echo "[xhs-skill] Cloning upstream repo into $UPSTREAM_DIR"
  git clone "$UPSTREAM_REPO" "$UPSTREAM_DIR"
else
  echo "[xhs-skill] Using existing upstream repo at $UPSTREAM_DIR"
fi

cd "$UPSTREAM_DIR"

python3 - <<'PY'
from pathlib import Path
p = Path('source/module/static.py')
if p.exists():
    text = p.read_text(encoding='utf-8')
    broken = '''PROJECT = f"XHS-Downloader V{VERSION_MAJOR}.{VERSION_MINOR} {
    'Beta' if VERSION_BETA else 'Stable'
}"'''
    fixed = '''PROJECT = f"XHS-Downloader V{VERSION_MAJOR}.{VERSION_MINOR} {'Beta' if VERSION_BETA else 'Stable'}"'''
    if broken in text:
        p.write_text(text.replace(broken, fixed), encoding='utf-8')
        print('[xhs-skill] Applied upstream syntax patch to source/module/static.py')
    else:
        print('[xhs-skill] Upstream syntax patch not needed')
else:
    print('[xhs-skill] Patch target not found; continuing')
PY

if command -v uv >/dev/null 2>&1 && [ -f uv.lock ]; then
  uv sync --no-dev
else
  python3 -m venv .venv
  . .venv/bin/activate
  python -m pip install --upgrade pip
  python -m pip install -r requirements.txt
fi

echo "[xhs-skill] Install complete"
echo "[xhs-skill] Upstream repo: $UPSTREAM_DIR"