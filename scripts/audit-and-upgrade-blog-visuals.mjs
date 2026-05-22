import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const sourceBlog = path.join(root, "_astro-source", "src", "content", "blog");
const publicVisuals = path.join(root, "_astro-source", "public", "blog-visuals");
const rootVisuals = path.join(root, "blog-visuals");
const auditDir = path.join(root, "site-agent");
const auditPath = path.join(auditDir, "codex-blog-image-audit-2026-05-22.md");

const priority = new Set([
  "canada-stablecoin-settlement",
  "web3-is-just-finance-infrastructure",
  "what-claude-cant-do-for-kyc",
  "ai-model-benchmark-cost",
  "finance-github-repos",
]);

function ensureDir(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function parsePost(file) {
  const raw = fs.readFileSync(file, "utf8");
  const match = raw.match(/^\uFEFF?---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
  if (!match) throw new Error(`Missing frontmatter: ${file}`);
  const fm = match[1];
  const body = match[2];
  const data = {};
  for (const line of fm.split(/\r?\n/)) {
    const idx = line.indexOf(":");
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    const value = line.slice(idx + 1).trim();
    data[key] = value.replace(/^"|"$/g, "");
  }
  const filenameSlug = path.basename(file, ".md");
  return { file, raw, fm, body, data, slug: data.slug || filenameSlug };
}

function imageExists(image) {
  if (!image) return false;
  const rel = image.replace(/^\//, "");
  return fs.existsSync(path.join(root, "_astro-source", "public", rel)) || fs.existsSync(path.join(root, rel));
}

function hasInfographic(body) {
  return /<iframe\s+src="\/blog-visuals\//i.test(body) || /<img\s+src="\/blog-visuals\//i.test(body);
}

function statusFor(post) {
  const hasHero = Boolean(post.data.image) && imageExists(post.data.image);
  const hasInfo = hasInfographic(post.body);
  if (hasHero && hasInfo) return "good";
  if (!hasHero) return "missing hero";
  return "missing infographic";
}

function escapeHtml(text) {
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function heroSvg({ title, kicker, chips = [], stat = "", note = "" }) {
  const chipText = chips.slice(0, 5).map((chip, i) => {
    const x = 70 + i * 170;
    return `<rect x="${x}" y="490" width="145" height="38" rx="19" fill="rgba(31,160,104,0.12)" stroke="rgba(31,160,104,0.45)"/><text x="${x + 18}" y="514" fill="#d7f8e8" font-size="18" font-family="Arial, sans-serif">${escapeHtml(chip)}</text>`;
  }).join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="#020204"/>
  <rect x="36" y="36" width="1128" height="558" rx="34" fill="#08080e" stroke="rgba(31,160,104,0.45)" stroke-width="2"/>
  <path d="M86 410 C230 330 350 460 492 360 S790 280 1088 342" fill="none" stroke="#1fa068" stroke-width="4" opacity="0.75"/>
  <path d="M86 450 C256 390 360 500 520 424 S810 360 1088 430" fill="none" stroke="#8a8aa0" stroke-width="2" opacity="0.35"/>
  <circle cx="990" cy="142" r="58" fill="rgba(31,160,104,0.12)" stroke="rgba(31,160,104,0.55)" stroke-width="2"/>
  <text x="990" y="136" fill="#1fa068" font-size="20" text-anchor="middle" font-family="Arial, sans-serif" font-weight="700">${escapeHtml(stat)}</text>
  <text x="990" y="166" fill="#8a8aa0" font-size="14" text-anchor="middle" font-family="Arial, sans-serif">${escapeHtml(note)}</text>
  <text x="70" y="108" fill="#1fa068" font-size="20" font-family="Arial, sans-serif" letter-spacing="3">${escapeHtml(kicker).toUpperCase()}</text>
  <foreignObject x="68" y="138" width="760" height="260">
    <div xmlns="http://www.w3.org/1999/xhtml" style="font-family: Arial, sans-serif; color:#e4e4ec; font-size:62px; line-height:1.02; font-weight:800; letter-spacing:0;">${escapeHtml(title)}</div>
  </foreignObject>
  ${chipText}
  <text x="70" y="560" fill="#8a8aa0" font-size="18" font-family="Arial, sans-serif">Bionic Banker field note</text>
</svg>`;
}

function visualHtml({ title, subtitle, cards = [], footer = "" }) {
  const cardHtml = cards.map((card) => `<article class="card">
    <span>${escapeHtml(card.kicker || "")}</span>
    <strong>${escapeHtml(card.title)}</strong>
    <p>${escapeHtml(card.body)}</p>
  </article>`).join("");
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  :root { color-scheme: dark; }
  body { margin:0; background:#020204; color:#e4e4ec; font-family: Arial, sans-serif; }
  .wrap { min-height:100vh; box-sizing:border-box; padding:34px; background: radial-gradient(circle at 80% 10%, rgba(31,160,104,.16), transparent 28%), #020204; }
  .shell { border:1px solid rgba(31,160,104,.35); border-radius:18px; padding:28px; background:rgba(8,8,14,.92); box-shadow:0 22px 80px rgba(0,0,0,.38); }
  .kicker { color:#1fa068; font-size:12px; letter-spacing:.16em; text-transform:uppercase; margin:0 0 10px; }
  h1 { font-size:clamp(30px, 5vw, 56px); line-height:1.02; margin:0; max-width:980px; letter-spacing:0; }
  .sub { color:#b8bbc9; max-width:880px; font-size:18px; line-height:1.55; margin:14px 0 24px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(210px, 1fr)); gap:14px; }
  .card { border:1px solid rgba(255,255,255,.09); border-radius:14px; padding:18px; background:rgba(255,255,255,.035); min-height:150px; }
  .card span { display:block; color:#1fa068; font-size:12px; text-transform:uppercase; letter-spacing:.12em; margin-bottom:14px; }
  .card strong { display:block; font-size:22px; line-height:1.15; margin-bottom:12px; }
  .card p { color:#b8bbc9; font-size:15px; line-height:1.45; margin:0; }
  .footer { margin-top:20px; color:#8a8aa0; font-size:14px; }
</style>
</head>
<body>
<main class="wrap">
  <section class="shell">
    <p class="kicker">Bionic Banker visual note</p>
    <h1>${escapeHtml(title)}</h1>
    <p class="sub">${escapeHtml(subtitle)}</p>
    <div class="grid">${cardHtml}</div>
    <p class="footer">${escapeHtml(footer)}</p>
  </section>
</main>
</body>
</html>`;
}

const upgrades = {
  "canada-stablecoin-settlement": {
    image: "/blog-visuals/canada-stablecoin-settlement/hero.svg",
    hero: { title: "Canada stablecoin settlement", kicker: "Stablecoin rails", chips: ["Wealthsimple", "Visa", "CADD", "Open banking"], stat: "2026", note: "pilot signal" },
    replacements: {
      "<!-- INFOGRAPHIC: stablecoin-settlement-map - pending render -->": {
        file: "settlement-map.html",
        height: 560,
        title: "Same compliance. Shorter settlement path.",
        subtitle: "The interesting part is not that value moved on-chain. It is that the compliance wrapper stayed in place while the settlement leg got shorter.",
        cards: [
          { kicker: "Traditional", title: "Authorization first", body: "Card networks can authorize quickly, but clearing and settlement still move through layered institutional processes." },
          { kicker: "Pilot", title: "Settlement leg changes", body: "A regulated fintech and payment network tested whether stablecoin rails can compress the slow part." },
          { kicker: "Still required", title: "Trust layer remains", body: "KYC, reporting, reconciliation, and institutional controls do not disappear. They become the wrapper around faster rails." }
        ],
        footer: "The win is not replacing finance. The win is making one slow layer easier to reconcile."
      },
      "<!-- INFOGRAPHIC: canada-stablecoin-timeline - pending render -->": {
        file: "canada-timeline.html",
        height: 520,
        title: "Why Canada took years to get here",
        subtitle: "The technology existed before the liability shape was comfortable enough for regulated adoption.",
        cards: [
          { kicker: "2015", title: "Ethereum rails", body: "Smart contract infrastructure becomes widely visible." },
          { kicker: "2018", title: "USDC arrives", body: "A regulated dollar token gives institutions a clearer settlement object." },
          { kicker: "2026", title: "Canadian pilot", body: "The conversation shifts from whether stablecoins work to where they fit." }
        ],
        footer: "Financial infrastructure usually moves when risk becomes legible, not when technology first appears."
      },
      "<!-- INFOGRAPHIC: open-banking-stablecoin-stack - pending render -->": {
        file: "open-banking-stack.html",
        height: 560,
        title: "The possible Canadian stack",
        subtitle: "Open banking and regulated stablecoins point toward cleaner movement from bank accounts into faster settlement rails.",
        cards: [
          { kicker: "1", title: "Bank account", body: "The deposit and customer relationship stay inside regulated finance." },
          { kicker: "2", title: "Permissioned access", body: "Consent and payment initiation make the funding leg cleaner." },
          { kicker: "3", title: "CAD stablecoin settlement", body: "The settlement leg becomes faster, more inspectable, and easier to reconcile." }
        ],
        footer: "Banks still matter. The middle gets compressed."
      }
    }
  },
  "web3-is-just-finance-infrastructure": {
    image: "/blog-visuals/web3-is-just-finance-infrastructure/hero.svg",
    hero: { title: "Web3 is finance infrastructure", kicker: "Translation table", chips: ["Circle", "Fireblocks", "Ondo", "Morpho", "Alchemy"], stat: "5", note: "functions" },
    replacements: {
      "<!-- INFOGRAPHIC: web3-tradfi-table - pending render -->": {
        file: "translation-table.html",
        height: 620,
        title: "Different names. Familiar functions.",
        subtitle: "The useful read is not crypto versus finance. It is which financial function each company is rebuilding.",
        cards: [
          { kicker: "Settlement", title: "Circle", body: "Dollar movement and redemption logic around USDC." },
          { kicker: "Custody", title: "Fireblocks", body: "Permissions, controls, and transfer safety for digital assets." },
          { kicker: "Credit", title: "Morpho", body: "Collateralized lending markets with on-chain pricing." },
          { kicker: "Rails", title: "Alchemy", body: "Developer infrastructure for financial applications." }
        ],
        footer: "The functions are old. The substrate is new."
      },
      "<!-- INFOGRAPHIC: five-functions-radial - pending render -->": {
        file: "five-functions.html",
        height: 560,
        title: "Finance keeps doing five things",
        subtitle: "Move money, hold assets, make credit, price risk, and build rails. Web3 survives where it does one of these better.",
        cards: [
          { kicker: "01", title: "Move money", body: "Stablecoins, messaging, bridges, and payment rails." },
          { kicker: "02", title: "Hold assets", body: "Custody, permissions, policy controls, and recovery." },
          { kicker: "03", title: "Make credit", body: "Collateral, lending markets, and programmable constraints." },
          { kicker: "04", title: "Price risk", body: "Risk engines, event markets, and stress testing." }
        ],
        footer: "The rails are new. The physics are not."
      }
    }
  },
  "what-claude-cant-do-for-kyc": {
    image: "/blog-visuals/what-claude-cant-do-for-kyc/hero.svg",
    hero: { title: "KYC is not a document demo", kicker: "Compliance systems", chips: ["Identity", "Screening", "Review", "Audit"], stat: "8", note: "steps" },
    replacements: {
      "<!-- INFOGRAPHIC: kyc-production-chain - pending render -->": {
        file: "production-chain.html",
        height: 620,
        title: "KYC is an eight-step production chain",
        subtitle: "AI helps with extraction, but the bank still needs screening, review, evidence, audit, and monitoring.",
        cards: [
          { kicker: "Demo layer", title: "Collect and extract", body: "Documents become fields. Useful, but only the front door." },
          { kicker: "Control layer", title: "Screen and verify", body: "Sanctions, PEP, adverse media, authenticity, and liveness checks." },
          { kicker: "Decision layer", title: "Review and preserve", body: "Exceptions, reviewer decisions, reason codes, and audit trail." },
          { kicker: "Live layer", title: "Monitor after onboarding", body: "Risk changes after the account opens. The system has to keep watching." }
        ],
        footer: "A model can read. A compliance system has to prove."
      },
      "<!-- INFOGRAPHIC: aml-engine-placement - pending render -->": {
        file: "aml-placement.html",
        height: 560,
        title: "Where the AML Engine fits",
        subtitle: "It does not verify identity documents. It belongs near transaction behavior and ongoing monitoring.",
        cards: [
          { kicker: "Not this", title: "Passport reader", body: "Identity extraction and document checks are a different layer." },
          { kicker: "This", title: "Behavior risk", body: "Counterparties, movement patterns, exposure, and changing behavior." },
          { kicker: "Why it matters", title: "Proof survives later", body: "Risk decisions need evidence that a reviewer or auditor can inspect." }
        ],
        footer: "Put each system where it belongs."
      }
    }
  },
  "ai-model-benchmark-cost": {
    image: "/blog-visuals/ai-model-benchmark-cost/hero.svg",
    hero: { title: "Read the cost column", kicker: "AI benchmark economics", chips: ["Score", "Cost", "Tasks", "Scale"], stat: "20x", note: "cost gap" },
    insertAfter: "But I work in finance, and the first thing they teach you when you read a table of numbers is: what column is everyone ignoring?",
    insert: {
      file: "score-per-dollar.html",
      height: 560,
      title: "The leaderboard has a hidden column",
      subtitle: "The best score is not always the best operating choice. At scale, cost per useful task becomes the decision.",
      cards: [
        { kicker: "Top score", title: "64.8% at $11.02", body: "A clean winner if you only read the performance column." },
        { kicker: "Efficient point", title: "63.2% at $0.55", body: "Almost the same score at a radically different cost profile." },
        { kicker: "Builder lens", title: "Score per dollar", body: "The right model depends on the task, the failure cost, and the run rate." }
      ],
      footer: "When systems run every day, the cost column stops being trivia."
    }
  },
  "finance-github-repos": {
    image: "/blog-visuals/finance-github-repos/hero.svg",
    hero: { title: "Elite finance ships infrastructure", kicker: "Open-source finance", chips: ["Jane Street", "Goldman", "JPMorgan", "BlackRock"], stat: "7", note: "repos" },
    insertAfter: "I went through seven of them, one from each firm. Here's what caught my attention and why.",
    insert: {
      file: "repo-map.html",
      height: 620,
      title: "What elite finance open-sources",
      subtitle: "The public repos are not flashy demos. They are infrastructure problems that show what expensive engineering teams care about.",
      cards: [
        { kicker: "Latency", title: "Jane Street", body: "Instruction-level tracing when estimation is not good enough." },
        { kicker: "Pricing", title: "Goldman Sachs", body: "Derivative pricing code from a desk-level quant environment." },
        { kicker: "Streaming", title: "JPMorgan", body: "Real-time data visualization built for market speed." },
        { kicker: "Optimization", title: "BlackRock", body: "Portfolio solvers where scale and constraints are the real problem." }
      ],
      footer: "The moat is not only the strategy. It is the infrastructure that lets the strategy run."
    }
  }
};

function addImageFrontmatter(post, image) {
  if (/^image:\s*/m.test(post.fm)) return post.raw.replace(/^image:\s*.*$/m, `image: "${image}"`);
  const lines = post.raw.split(/\r?\n/);
  const categoryIdx = lines.findIndex((line) => line.startsWith("category:"));
  const insertAt = categoryIdx >= 0 ? categoryIdx + 1 : lines.findIndex((line, idx) => idx > 0 && line === "---");
  lines.splice(insertAt, 0, `image: "${image}"`);
  return lines.join("\n");
}

function iframeFor(slug, file, height, title) {
  return `<div class="embed-visual">
  <iframe src="/blog-visuals/${slug}/${file}" title="${escapeHtml(title)}" style="width:100%;min-height:${height}px;border:none;border-radius:12px;" loading="lazy"></iframe>
</div>`;
}

function writeVisualPair(slug, file, content) {
  const dirs = [path.join(publicVisuals, slug), path.join(rootVisuals, slug)];
  for (const dir of dirs) {
    ensureDir(dir);
    fs.writeFileSync(path.join(dir, file), content, "utf8");
  }
}

function upgradePost(post) {
  const cfg = upgrades[post.slug];
  if (!cfg) return false;
  let next = addImageFrontmatter(post, cfg.image);
  writeVisualPair(post.slug, "hero.svg", heroSvg(cfg.hero));

  if (cfg.replacements) {
    for (const [marker, visual] of Object.entries(cfg.replacements)) {
      writeVisualPair(post.slug, visual.file, visualHtml(visual));
      next = next.replace(marker, iframeFor(post.slug, visual.file, visual.height, visual.title));
    }
  }

  if (cfg.insert && cfg.insertAfter && !next.includes(`/blog-visuals/${post.slug}/${cfg.insert.file}`)) {
    writeVisualPair(post.slug, cfg.insert.file, visualHtml(cfg.insert));
    next = next.replace(cfg.insertAfter, `${cfg.insertAfter}\n\n${iframeFor(post.slug, cfg.insert.file, cfg.insert.height, cfg.insert.title)}`);
  }

  fs.writeFileSync(post.file, next, "utf8");
  return true;
}

const posts = fs.readdirSync(sourceBlog)
  .filter((file) => file.endsWith(".md"))
  .map((file) => parsePost(path.join(sourceBlog, file)))
  .sort((a, b) => new Date(b.data.date || 0).getTime() - new Date(a.data.date || 0).getTime());

const before = posts.map((post) => ({
  slug: post.slug,
  title: post.data.title,
  date: post.data.date,
  status: statusFor(post),
  priority: priority.has(post.slug),
}));

for (const post of posts) upgradePost(post);

const afterPosts = fs.readdirSync(sourceBlog)
  .filter((file) => file.endsWith(".md"))
  .map((file) => parsePost(path.join(sourceBlog, file)))
  .sort((a, b) => new Date(b.data.date || 0).getTime() - new Date(a.data.date || 0).getTime());

const after = afterPosts.map((post) => ({
  slug: post.slug,
  title: post.data.title,
  date: post.data.date,
  status: statusFor(post),
  priority: priority.has(post.slug),
}));

const countBy = (rows) => rows.reduce((acc, row) => {
  acc[row.status] = (acc[row.status] || 0) + 1;
  return acc;
}, {});

const lines = [
  "# Bionic Banker Blog Image Audit",
  "",
  "Generated: `2026-05-22`",
  "",
  "Scope: Astro source posts that are currently publishable. Status means:",
  "",
  "- `good`: frontmatter image exists and the article has at least one rendered visual.",
  "- `missing hero`: no working frontmatter image for article cards and social preview.",
  "- `missing infographic`: hero exists, but the body does not include a rendered visual.",
  "",
  "## Summary Before Upgrade",
  "",
  `- good: ${countBy(before).good || 0}`,
  `- missing hero: ${countBy(before)["missing hero"] || 0}`,
  `- missing infographic: ${countBy(before)["missing infographic"] || 0}`,
  "",
  "## Priority Upgrades Completed",
  "",
  "| Post | Before | After |",
  "|---|---|---|",
  ...after.filter((row) => row.priority).map((row) => {
    const prior = before.find((item) => item.slug === row.slug);
    return `| ${row.slug} | ${prior?.status || "unknown"} | ${row.status} |`;
  }),
  "",
  "## Full Audit After Upgrade",
  "",
  "| Status | Date | Slug | Title |",
  "|---|---|---|---|",
  ...after.map((row) => `| ${row.status} | ${row.date || ""} | \`${row.slug}\` | ${row.title || ""} |`),
  "",
  "## Next Visual Queue",
  "",
  "1. Upgrade newest `missing hero` posts next so the archive stops showing text-only cards.",
  "2. Add at least one body infographic to any `missing infographic` post with existing hero art.",
  "3. Prefer Bionic Banker-owned diagrams over raw company logo grids unless the image is official, source-linked, and not framed as endorsement.",
  ""
];

ensureDir(auditDir);
fs.writeFileSync(auditPath, lines.join("\n"), "utf8");
console.log(`Wrote ${auditPath}`);
