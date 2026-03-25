#!/usr/bin/env python3
import argparse, json, re, sys, urllib.request

URL_RE = re.compile(r'(https?://(?:www\.)?xiaohongshu\.com/[^\s]+|https?://xhslink\.com/[^\s]+)')

def call(server, payload):
    req = urllib.request.Request(
        server,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST',
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read().decode('utf-8', errors='replace')
        try:
            return json.loads(body)
        except Exception:
            return {'raw': body}

p = argparse.ArgumentParser()
p.add_argument('--server', default='http://127.0.0.1:5556/xhs/detail')
p.add_argument('--url', action='append', default=[])
p.add_argument('--file')
p.add_argument('--stdin', action='store_true')
p.add_argument('--download', action='store_true')
p.add_argument('--cookie')
p.add_argument('--proxy')
p.add_argument('--skip', action='store_true')
p.add_argument('--out')
p.add_argument('--jsonl', action='store_true')
p.add_argument('--concurrency', type=int, default=1)
args = p.parse_args()

items = []
items.extend(args.url)
if args.file:
    items.append(open(args.file, encoding='utf-8').read())
if args.stdin:
    items.append(sys.stdin.read())

urls = []
for item in items:
    found = URL_RE.findall(item)
    if found:
        urls.extend(found)
    elif item.strip().startswith('http'):
        urls.append(item.strip())

# dedupe preserving order
seen = set()
ordered = []
for u in urls:
    if u not in seen:
        seen.add(u)
        ordered.append(u)

results = []
for u in ordered:
    payload = {'url': u}
    if args.download:
        payload['download'] = True
    if args.cookie:
        payload['cookie'] = args.cookie
    if args.proxy:
        payload['proxy'] = args.proxy
    if args.skip:
        payload['skip'] = True
    try:
        res = call(args.server, payload)
        results.append({'input_url': u, 'ok': True, 'response': res})
    except Exception as e:
        results.append({'input_url': u, 'ok': False, 'error': str(e)})

if args.jsonl:
    text = '\n'.join(json.dumps(item, ensure_ascii=False) for item in results)
else:
    text = json.dumps(results, ensure_ascii=False, indent=2)

if args.out:
    with open(args.out, 'w', encoding='utf-8') as f:
        f.write(text)
else:
    print(text)
