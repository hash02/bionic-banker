"""
SEO Injector - bionicbanker.tech
Injects og:image, twitter:image, and JSON-LD Article structured data into all articles.
Modes: --dry-run (show changes) | --apply (modify files)
Pure Python — no external dependencies.
"""
import os, re, sys, io, json

# Fix Windows console encoding (skip if already wrapped or on CI)
try:
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
except Exception:
    pass

BB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = {"index.html", "articles.html", "preview-layout.html", "agent-architecture.html", "dashboard_preview.html"}
BASE_URL = "https://bionicbanker.tech"

MODE = "dry-run"
if "--apply" in sys.argv:
    MODE = "apply"


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def extract_title(content):
    """Extract title, strip ' — Bionic Banker' suffix."""
    m = re.search(r"<title>([^<]+)</title>", content)
    if not m:
        return ""
    title = m.group(1).strip()
    return re.sub(r"\s*[—–-]\s*Bionic Banker\s*$", "", title)


def extract_description(content):
    m = re.search(r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']', content)
    return m.group(1).strip() if m else ""


def extract_date(content):
    """Extract date from article-date span. 'March 2026' → '2026-03-01'."""
    m = re.search(r'class="article-date"[^>]*>([^<]+)<', content)
    if not m:
        return ""
    date_text = m.group(1).strip()

    months = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }

    for month_name, month_num in months.items():
        if month_name in date_text:
            year_m = re.search(r"(\d{4})", date_text)
            if year_m:
                return f"{year_m.group(1)}-{month_num}-01"

    return ""


def get_image_url(slug):
    """Get the og:image URL for an article."""
    if slug == "aml-roaster":
        return f"{BASE_URL}/blog-visuals/png/01-hero-banner.png"
    return f"{BASE_URL}/blog-visuals/{slug}/social-preview.png"


def build_jsonld(slug, title, description, date_published, image_url):
    """Build JSON-LD Article structured data."""
    data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": description,
        "image": image_url,
        "author": {
            "@type": "Person",
            "name": "HASH",
            "url": BASE_URL
        },
        "publisher": {
            "@type": "Organization",
            "name": "Bionic Banker",
            "url": BASE_URL
        },
        "datePublished": date_published or "2026-01-01",
        "dateModified": date_published or "2026-01-01",
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"{BASE_URL}/{slug}.html"
        }
    }
    return json.dumps(data, indent=2)


def inject_seo(filepath, slug):
    """Inject og:image, twitter:image, and JSON-LD. Returns (modified_content, changes_list)."""
    content = read_file(filepath)
    changes = []
    image_url = get_image_url(slug)

    # 1. Handle og:image
    existing_og_image = re.search(r'<meta\s+property=["\']og:image["\']\s+content=["\']([^"\']*)["\']', content)
    if existing_og_image:
        old_url = existing_og_image.group(1)
        if not old_url.startswith("http"):
            # Update to full URL
            content = content.replace(existing_og_image.group(0),
                f'<meta property="og:image" content="{image_url}" />')
            changes.append(f"og:image updated: {old_url} → {image_url}")
    else:
        # Insert after og:description or og:title, or before </head>
        og_insert = f'    <meta property="og:image" content="{image_url}" />\n'
        og_desc = re.search(r'(<meta\s+property=["\']og:description["\'][^>]*/?>)\s*\n', content)
        og_title = re.search(r'(<meta\s+property=["\']og:title["\'][^>]*/?>)\s*\n', content)
        if og_desc:
            content = content.replace(og_desc.group(0), og_desc.group(0) + og_insert)
        elif og_title:
            content = content.replace(og_title.group(0), og_title.group(0) + og_insert)
        else:
            content = content.replace("</head>", og_insert + "  </head>")
        changes.append(f"og:image added: {image_url}")

    # 2. Handle twitter:image
    existing_tw_image = re.search(r'<meta\s+name=["\']twitter:image["\']\s+content=["\']([^"\']*)["\']', content)
    if not existing_tw_image:
        tw_insert = f'    <meta name="twitter:image" content="{image_url}" />\n'
        tw_desc = re.search(r'(<meta\s+name=["\']twitter:description["\'][^>]*/?>)\s*\n', content)
        tw_title = re.search(r'(<meta\s+name=["\']twitter:title["\'][^>]*/?>)\s*\n', content)
        tw_card = re.search(r'(<meta\s+name=["\']twitter:card["\'][^>]*/?>)\s*\n', content)
        if tw_desc:
            content = content.replace(tw_desc.group(0), tw_desc.group(0) + tw_insert)
        elif tw_title:
            content = content.replace(tw_title.group(0), tw_title.group(0) + tw_insert)
        elif tw_card:
            content = content.replace(tw_card.group(0), tw_card.group(0) + tw_insert)
        else:
            content = content.replace("</head>", tw_insert + "  </head>")
        changes.append(f"twitter:image added")

    # 3. Handle JSON-LD
    existing_jsonld = re.search(r'<script\s+type=["\']application/ld\+json["\']', content)
    if not existing_jsonld:
        title = extract_title(content)
        description = extract_description(content)
        date = extract_date(content)
        jsonld = build_jsonld(slug, title, description, date, image_url)
        jsonld_block = f'    <script type="application/ld+json">\n{jsonld}\n    </script>\n'
        content = content.replace("</head>", jsonld_block + "  </head>")
        changes.append(f"JSON-LD added (date: {date or 'unknown'})")

    return content, changes


def main():
    htmls = [f for f in os.listdir(BB) if f.endswith(".html") and f not in SKIP]
    total_changes = 0

    print(f"SEO Injector — Mode: {MODE}\n")

    for f in sorted(htmls):
        slug = f.replace(".html", "")
        filepath = os.path.join(BB, f)
        new_content, changes = inject_seo(filepath, slug)

        if changes:
            total_changes += len(changes)
            print(f"{'[DRY RUN] ' if MODE == 'dry-run' else ''}  {f}:")
            for c in changes:
                print(f"    + {c}")
            if MODE == "apply":
                write_file(filepath, new_content)
        else:
            print(f"  {f}: no changes needed")

    print(f"\n{'Would make' if MODE == 'dry-run' else 'Made'} {total_changes} changes across {len(htmls)} files")
    if MODE == "dry-run":
        print("\nRun with --apply to modify files")


if __name__ == "__main__":
    main()
