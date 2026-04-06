"""Export HTML infographics to PNG using Playwright."""

import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright

INFOGRAPHIC_DIR = (
    Path(__file__).parent
    / "_astro-source"
    / "public"
    / "blog-visuals"
    / "agentic-ai-banking"
)
OUTPUT_DIR = INFOGRAPHIC_DIR
WIDTH = 1200
HEIGHT = 630


async def export_html_to_png(html_path: Path, output_path: Path) -> None:
    """Render a single HTML file to PNG at 2x retina."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": WIDTH, "height": HEIGHT},
            device_scale_factor=2,
        )
        await page.goto(f"file://{html_path.resolve()}", wait_until="networkidle")
        # Wait for fonts and animations to settle
        await page.wait_for_timeout(2000)
        await page.screenshot(
            path=str(output_path),
            clip={"x": 0, "y": 0, "width": WIDTH, "height": HEIGHT},
        )
        await browser.close()
        print(
            f"  exported: {output_path.name} ({output_path.stat().st_size // 1024}KB)"
        )


async def main() -> None:
    html_files = sorted(INFOGRAPHIC_DIR.glob("*.html"))
    if not html_files:
        print("No HTML files found!")
        sys.exit(1)

    print(f"Exporting {len(html_files)} infographics from {INFOGRAPHIC_DIR}")
    for html_file in html_files:
        png_name = html_file.stem + ".png"
        output_path = OUTPUT_DIR / png_name
        await export_html_to_png(html_file, output_path)

    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())
