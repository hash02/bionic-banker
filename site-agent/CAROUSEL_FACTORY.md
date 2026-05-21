# Carousel Factory

This is the repeatable path for turning one content brief into social-ready slides.

## Flow

1. Write one JSON brief in `site-agent/carousel-briefs/`.
2. Run `scripts/build-carousel.ps1`.
3. The script sends the brief to the render host, pulls back `slide-*.png` plus one PDF, verifies the output, and optionally commits the assets.

No social posting happens here. This factory only creates the visual package.

## Setup

Set these in your local shell or profile. Keep real host names, keys, and machine details out of the repo.

```powershell
$env:BB_CAROUSEL_REMOTE = "user@host"
$env:BB_CAROUSEL_SSH_KEY = "C:\path\to\key"
```

## Commands

Validate a brief without rendering:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build-carousel.ps1 -Brief .\site-agent\carousel-briefs\ai-benchmark-carousel.json -Slug ai-benchmark-carousel -ValidateOnly
```

Render and commit:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build-carousel.ps1 -Brief .\site-agent\carousel-briefs\ai-benchmark-carousel.json -Slug ai-benchmark-carousel -Commit
```

## Channel Map

LinkedIn gets the PDF carousel. Use the article link in the first comment.

Bionic Banker gets the article as the home base. Use `slide-01.png` as a share image and keep the PDF in `/blog-visuals/<slug>/`.

GitHub profile or repo README gets one clean slide image plus the article link when it helps explain the work.

Dev.to or Hashnode can reuse the article idea, but Bionic Banker stays the canonical page. Use one image, then link back.

Telegram gets one strongest slide plus the article link.

## Backup Lane

The render host is useful because it already has the browser tooling and graphics path. The next hardening move is a second render host with the same `build_carousel.py` command, then this script can switch hosts by changing `BB_CAROUSEL_REMOTE`.

Keep every carousel recoverable from three things: the brief JSON, the generated asset folder, and the Git commit.
