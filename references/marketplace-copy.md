# Marketplace Copy

## Title
xhs-downloader-skill

## One-line description
Run JoeanAmier/XHS-Downloader as a reusable OpenClaw skill for Xiaohongshu/RedNote metadata extraction, media URL extraction, and batch link processing.

## Short description
Use this skill when you want to process Xiaohongshu links reliably through a local API workflow instead of manual browser extraction. Supports single links, xhslink short links, pasted text blobs, and batch processing.

## What it does
- Installs and runs XHS-Downloader locally
- Starts API mode on port 5556
- Extracts metadata from Xiaohongshu posts
- Resolves xhslink.com short links
- Extracts media download URLs
- Processes many links in one batch

## Best for
- Bot workflows
- Batch link processing
- Xiaohongshu research pipelines
- Structured JSON extraction
- Future download automation

## Verified in validation
- Local venv install
- API mode boot
- Real xhslink resolution
- Metadata extraction
- Media URL extraction
- Mixed-success batch behavior

## Known limitation note
This skill includes a documented local upstream patch for a syntax error encountered during validation. See `references/upstream-patch.md`.

## Example invocations
- "Use xhs-downloader-skill to fetch metadata for this xhslink"
- "Use xhs-downloader-skill to batch process these 20 Xiaohongshu links"
- "Use xhs-downloader-skill to extract media URLs from these pasted RedNote links"
