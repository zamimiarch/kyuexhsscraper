#!/usr/bin/env python3
import argparse, json, sys, urllib.request

p = argparse.ArgumentParser()
p.add_argument('--server', default='http://127.0.0.1:5556/xhs/detail')
p.add_argument('--url', required=True)
p.add_argument('--download', action='store_true')
p.add_argument('--index', nargs='*', type=int)
p.add_argument('--cookie')
p.add_argument('--proxy')
p.add_argument('--skip', action='store_true')
args = p.parse_args()

payload = {'url': args.url}
if args.download:
    payload['download'] = True
if args.index:
    payload['index'] = args.index
if args.cookie:
    payload['cookie'] = args.cookie
if args.proxy:
    payload['proxy'] = args.proxy
if args.skip:
    payload['skip'] = True

req = urllib.request.Request(
    args.server,
    data=json.dumps(payload).encode('utf-8'),
    headers={'Content-Type': 'application/json'},
    method='POST',
)
with urllib.request.urlopen(req, timeout=30) as r:
    body = r.read().decode('utf-8', errors='replace')
    try:
        obj = json.loads(body)
        print(json.dumps(obj, ensure_ascii=False, indent=2))
    except Exception:
        print(body)
