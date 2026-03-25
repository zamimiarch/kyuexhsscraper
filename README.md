# kyuexhsscraper

OpenClaw skill for installing and operating XHS-Downloader for Xiaohongshu/RedNote extraction and downloads.

Primary entrypoint: `SKILL.md`

## What this repo contains

- `SKILL.md` — instructions for OpenClaw / agent use
- `scripts/install.sh` — clones the upstream downloader locally and installs dependencies
- `scripts/start_api.sh` — starts the local API server
- `scripts/call_detail.py` — sends one detail request to the API
- `scripts/call_batch.py` — sends batch requests to the API
- `references/` — validation notes, examples, and upstream patch context

## Standalone usage

This repo is self-bootstrapping.

```bash
bash scripts/install.sh
bash scripts/start_api.sh
```

In another shell:

```bash
python3 scripts/call_detail.py --url 'https://www.xiaohongshu.com/explore/EXAMPLE'
```

## Notes

- The installer clones the upstream project into `vendor/XHS-Downloader` by default.
- You can override the upstream location with `XHS_DOWNLOADER_DIR=/path/to/XHS-Downloader`.
- A known upstream syntax issue is patched automatically during install when present.
- Some Xiaohongshu posts require cookies or other access context; metadata fetches may fail without them even when the local API is working correctly.
