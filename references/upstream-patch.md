# Upstream Patch Note

## Local patch applied during validation

Repository:
- `JoeanAmier/XHS-Downloader`

Local file patched:
- `/root/.openclaw/workspace/tmp/XHS-Downloader/source/module/static.py`

## Problem

The cloned source contained a broken multiline f-string:

```python
PROJECT = f"XHS-Downloader V{VERSION_MAJOR}.{VERSION_MINOR} {
    'Beta' if VERSION_BETA else 'Stable'
}"
```

This caused runtime failure on import:
- `SyntaxError: unterminated string literal`

## Local fix applied

Replaced with:

```python
PROJECT = f"XHS-Downloader V{VERSION_MAJOR}.{VERSION_MINOR} {'Beta' if VERSION_BETA else 'Stable'}"
```

## Why this matters

Without this fix, API mode could not boot in local validation.
If publishing this skill for reuse, either:
1. document this patch clearly, or
2. point the skill at a fork/commit where the issue is fixed.


## Additional compatibility note

In Python 3.11 environments, `pathlib.Path.walk()` is unavailable.
A compatibility patch replacing it with `os.walk()` may be required in:
- `source/expansion/file_folder.py`

This affects cleanup/shutdown paths rather than the core request flow, but it can cause noisy crashes after startup failures.
