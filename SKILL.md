---
name: xhs-downloader-skill
description: Install, run, and operate JoeanAmier/XHS-Downloader for Xiaohongshu/RedNote link extraction, metadata retrieval, download URL extraction, and media downloading. Use when the user wants to fetch or download Xiaohongshu posts, run XHS-Downloader locally in CLI/API mode, set up a reusable downloader workflow, or wrap the repo into a repeatable OpenClaw skill.
---

# xhs-downloader-skill

Use this skill to operate the `JoeanAmier/XHS-Downloader` repository as a repeatable local tool.

Keep the workflow thin:
- Prefer the upstream repo for core functionality
- Use local helper scripts only for setup and stable invocation
- Prefer API mode for repeatable automation
- Use CLI mode for one-off manual downloads

## Quick Start

Default upstream checkout location after install:
- `vendor/XHS-Downloader`
- Override with `XHS_DOWNLOADER_DIR=/path/to/XHS-Downloader` if needed

Skill helper scripts:
- `scripts/install.sh` — install dependencies with `uv` if available, else local venv
- `scripts/start_api.sh` — start API mode on port `5556`
- `scripts/call_detail.py` — call `/xhs/detail` for a single URL
- `scripts/call_batch.py` — process many URLs from repeated flags, file input, or pasted text blobs

Default local API:
- Base URL: `http://127.0.0.1:5556`
- Docs: `http://127.0.0.1:5556/docs`
- Endpoint: `POST /xhs/detail`

## Workflow

### 1. Install dependencies

Run:

```bash
bash scripts/install.sh
```

Notes:
- This clones the upstream downloader into `vendor/XHS-Downloader` if it is not already present
- Prefer `uv sync --no-dev` when `uv` exists
- Fallback to a local `.venv` with `pip install -r requirements.txt`
- Do not global-install Python packages unless necessary
- Applies the known upstream syntax patch automatically if needed

### 2. Start API mode

Run:

```bash
bash scripts/start_api.sh
```

This starts:

```bash
python main.py api
```

Use API mode when:
- You want structured JSON responses
- You want repeatable automation
- You want to call the downloader from scripts or future workflows

### 3. Request work metadata or downloads

Use for a single URL:

```bash
python scripts/call_detail.py --url '<xhs-url>'
```

Common variants:

```bash
python scripts/call_detail.py --url '<xhs-url>' --download
python scripts/call_detail.py --url '<xhs-url>' --download --index 1 3 5
python scripts/call_detail.py --url '<xhs-url>' --cookie 'a1=...; web_session=...'
python scripts/call_detail.py --url '<xhs-url>' --proxy 'http://127.0.0.1:7890'
```

Use for batch URLs:

```bash
python scripts/call_batch.py --url '<xhs-url-1>' --url '<xhs-url-2>'
python scripts/call_batch.py --file links.txt
cat links.txt | python scripts/call_batch.py --stdin
```

Batch behavior:
- Accept raw Xiaohongshu URLs and `xhslink.com` short links
- Extract links from pasted text blobs
- Deduplicate inputs
- Return one JSON array of result objects by default
- Support `--jsonl` output for line-oriented pipelines
- Expose `--concurrency` as a forward-compatible flag for future throughput tuning

## Decision Rules

### Prefer API mode when
- The user wants a reusable workflow
- The task may be repeated many times
- You need machine-readable output
- You want the repo to behave like a service/tool

### Prefer CLI/TUI mode when
- The user wants a manual local run
- You are testing interactively
- You only need a one-off download

## Parameters worth knowing

From upstream API docs:
- `url` (required): Xiaohongshu post URL
- `download` (bool): whether to download files
- `index` (list[int]): download specific image numbers for image posts
- `cookie` (str): optional cookie to improve access / quality
- `proxy` (str): optional proxy
- `skip` (bool): skip already-downloaded items

## Verified Capabilities

Validated locally in this environment:
- Install dependencies in a local venv
- Start XHS-Downloader in API mode
- Resolve `xhslink.com` short links
- Fetch post metadata successfully
- Extract media download URLs from a real Xiaohongshu post

## Known Limitations

- Installer auto-applies one known upstream syntax fix when present; see `references/upstream-patch.md`
- Cookie-less runs may return incomplete data, lower-quality media, or outright fetch failures on some posts
- Batch helper currently emits JSON arrays only; CSV/JSONL can be added later if needed
- Download mode is supported by upstream API, but should be verified separately when file persistence matters

## Output Handling

When calling the API:
- Return parsed JSON to the user when small
- If downloads are enabled, tell the user where files landed
- If auth/cookie issues appear, surface that clearly
- Do not pretend downloads succeeded without checking file output or response payload

## Cookie Guidance

The upstream repo notes:
- Cookie is optional
- Without cookie, some features may fail or return lower-quality video
- If results look incomplete, ask for a cookie-backed run

Do not invent cookie extraction flows. Use the repo’s documented approach or ask the user for a cookie string when needed.

## References

Read these only if needed:
- `references/upstream-notes.md` — concise summary of supported modes and API usage
- `references/upstream-patch.md` — local runtime patch required during validation

## Files in This Skill

### scripts/
- `install.sh`
- `start_api.sh`
- `call_detail.py`
- `call_batch.py`

### references/
- `upstream-notes.md`
