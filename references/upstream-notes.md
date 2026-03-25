# Upstream Notes — XHS-Downloader

Repository: JoeanAmier/XHS-Downloader
Local clone: `/root/.openclaw/workspace/tmp/XHS-Downloader`

## Useful modes

### CLI / TUI
Run:

```bash
python main.py
```

### API mode
Run:

```bash
python main.py api
```

Docs:
- `http://127.0.0.1:5556/docs`
- `http://127.0.0.1:5556/redoc`

Endpoint:
- `POST /xhs/detail`

JSON parameters:
- `url`: Xiaohongshu work URL
- `download`: whether to download files
- `index`: specific image indexes for image posts
- `cookie`: optional cookie
- `proxy`: optional proxy
- `skip`: skip existing download records

### MCP mode
Run:

```bash
python main.py mcp
```

## Notes

- Cookie is optional but often helpful
- Without cookie, some video downloads may be low quality or incomplete
- API mode is the best base for repeatable automation
- Use the repo for actual extraction/downloading logic; keep this skill wrapper small
