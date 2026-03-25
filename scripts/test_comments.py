#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = Path((ROOT / 'vendor' / 'XHS-Downloader').resolve())
sys.path.insert(0, str(UPSTREAM))

from source.application.app import XHS  # type: ignore


def main() -> int:
    parser = argparse.ArgumentParser(description='Test XHS comment fetch via local API helper')
    parser.add_argument('--url', required=True)
    parser.add_argument('--cookie', default='')
    parser.add_argument('--limit', type=int, default=50)
    args = parser.parse_args()

    xhs = XHS(cookie=args.cookie)

    async def run():
        links = await xhs.extract_links(args.url)
        if not links:
            raise RuntimeError('failed to resolve xhs link')
        note_url = links[0]
        note_id = xhs.extract_id([note_url])[0]
        result = await xhs.fetch_comments(note_url, cookie=args.cookie, limit=args.limit)
        payload = {
            'input_url': args.url,
            'resolved_url': note_url,
            'note_id': note_id,
            'comment_result': result,
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        await xhs.manager.close()

    import asyncio
    asyncio.run(run())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
