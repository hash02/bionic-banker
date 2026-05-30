# Bionic Banker Agent Instructions

## Mission

Bionic Banker is HASH's public thought platform. The caretaker job is to keep it publishing, technically healthy, and aligned with HASH's voice without changing the locked design system.

## Source Of Truth

- Production site: `bionicbanker.tech`
- Canonical repo: `hash02/bionic-banker`
- Content source: `_astro-source/src/content/blog/`
- Built production output: committed root-level HTML and assets
- Dashboard/status data: `dashboard-data/`

## Hard Rules

- Do not change visual design, layout, CSS, theme, typography, or hero structure unless HASH explicitly asks.
- Content changes are a two-file job when they affect live Astro pages: update source and built output.
- Verify article counts from files, not memory.
- No bank/company-negative framing in public content.
- No social media browser automation.
- Links should usually go in first comment for LinkedIn drafts, not the main post body.
- Every public claim about numbers, rules, counts, or dates must be computed from source.
- If a claim is uncertain, missing context, or only a best estimate, say so plainly. Do not write uncertain public claims as facts.
- Do not invent sources, URLs, studies, statistics, quotes, legal cases, company reports, or historical references. If a source is not checked, mark it as missing instead of filling it in.
- Public copy must follow `PUBLIC_COPY_STANDARD.md`: use serious risk/evidence/audit/control language, avoid the informal terms listed there in visible public surfaces, and keep legal/compliance/trading authority boundaries explicit.
- Before publishing public-copy changes, run `npm run test:public-copy` and `npm run test:epistemic-harness` from `_astro-source` and fix any blockers.
- Before publishing layout/navigation/dashboard changes, run `npm run qa:mobile` from `_astro-source`; inspect `qa-reports/latest/report.md` and screenshots when it fails.

## Caretaker Loop

Run this when asked to maintain Bionic Banker:

1. Check `git status --short --branch`.
2. Count current articles from content files.
3. Check latest drafts and whether one week has passed without publishing.
4. Check broken links or stale dashboard JSON when relevant.
5. Produce a short caretaker report:
   - site health
   - content gap
   - next publish candidate
   - blocked items
   - exact files to edit

## Publishing Workflow

1. Pick one post idea from current system evidence, not from loose intuition.
2. Draft in HASH voice: raw, conversational, specific.
3. Strip internal identifiers, paths, IPs, secrets, and private infrastructure details.
4. Update source content.
5. Update built output if the production topology requires it.
6. Run site validation or targeted smoke check.
7. Commit and push intentionally.

## Do Not Touch Without Approval

- Site design and layout.
- Cloudflare/production settings.
- GA tags, Formspree endpoint, or newsletter plumbing.
- Existing live pages outside the requested content scope.
- Any file that exposes internal agent names, server IPs, private paths, or credentials.

## Useful Reports

- Weekly content gap report.
- Draft queue report.
- Public claim verification report.
- Site health report.
- Distribution plan for one selected post.

