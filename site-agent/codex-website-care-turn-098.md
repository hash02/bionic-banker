# Codex Website Care Turn 098

Date: 2026-05-20
Actor: Codex
Previous actor: Claude Code

---

## Context — Why This Turn Exists

HASH did a strategic alignment check against Elon Musk's operating principles (The Book of Elon). The output:

Bionic Lab is the next unlock. It is the live proof piece that shifts the narrative from "content about AI in finance" to "live fintech operating layer you can actually use." Everything else is articles. Bionic Lab is the thing itself.

This turn has two jobs:
1. Execute all pending Bionic Lab turns in order (001 through 004)
2. Link Bionic Lab from the Bionic Banker homepage once it is deployed

---

## Task A: Execute Bionic Lab Turns in Order

Read and execute each of these turn files in strict sequence. Do not skip ahead. Do not run in parallel.

```
site-agent/codex-bionic-lab-turn-001.md  ← scaffold + shell + deploy
site-agent/codex-bionic-lab-turn-002.md  ← Financial Planning module
site-agent/codex-bionic-lab-turn-003.md  ← AML Monitor module
site-agent/codex-bionic-lab-turn-004.md  ← Signal Intelligence module
```

The scaffold files are partially created at:
```
C:\Users\himan\OneDrive\hash 2026\bionic-lab\
```

The following files already exist there (do not overwrite):
- package.json
- vite.config.ts
- tsconfig.json
- tsconfig.node.json
- postcss.config.js
- tailwind.config.ts
- index.html
- public/_redirects
- src/index.css
- src/main.tsx
- src/App.tsx
- src/components/Sidebar.tsx
- src/components/TopBar.tsx

Turn 001 will tell you what still needs to be created. Read it fully before acting.

After turn 001 is complete, the app must be:
- Git initialized at bionic-lab/
- Pushed to GitHub: hash02/bionic-lab (create repo if it does not exist)
- Connected to Cloudflare Pages
- Live at a Cloudflare Pages URL (note the URL in your report)

Then execute turns 002, 003, 004 in order. Each adds one module. Build and deploy after each.

---

## Task B: Add "Launch Lab" CTA to Bionic Banker Homepage

Once Bionic Lab is live (you have the Cloudflare Pages URL), add a launch button to the Bionic Banker homepage.

**R-039 applies: edit BOTH source AND built output.**

### Where to add it

Source file: `_astro-source/src/pages/index.astro`

Find the hero section. The current hero has a headline and a button/link area. Add a second button below the existing CTA:

```html
<a href="[BIONIC_LAB_URL]" target="_blank" rel="noopener noreferrer" class="launch-lab-btn">
  Launch Lab &rarr;
</a>
```

Replace `[BIONIC_LAB_URL]` with the actual Cloudflare Pages URL.

### Styling (add to global.css or inline in the hero section)

```css
.launch-lab-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.65rem 1.4rem;
  border: 1px solid #1fa068;
  color: #1fa068;
  font-family: var(--mono);
  font-size: 0.85rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-decoration: none;
  border-radius: 6px;
  transition: background 0.15s, color 0.15s;
}
.launch-lab-btn:hover {
  background: rgba(31, 160, 104, 0.1);
}
```

### Build and copy (R-039)

```bash
cd _astro-source && npm run build
```

Copy:
```
_astro-source/dist/index.html → index.html (repo root)
```

### Commit

```bash
git add _astro-source/src/pages/index.astro
git add _astro-source/public/styles/global.css
git add index.html
git commit -m "feat: add Launch Lab CTA linking to bionic-lab app"
git pull --rebase origin main
git push origin main
```

---

## Task C: Deploy Pending Articles (if not already done)

Check if turns 095 and 097 have been executed. If not, run them now:
- Turn 095: AI benchmark cost article
- Turn 097: Finance GitHub repos article + carousel

---

## Done State

Turn is complete when:
- Bionic Lab is live at a public URL with all 4 modules working
- "Launch Lab" button appears on bionicbanker.tech homepage and links to the live app
- Both pending articles are deployed
- Report back with: Bionic Lab URL, commit hashes, live URL confirmations

---

## Why This Matters (context for Codex)

HASH reviewed the Elon Musk operating playbook against his current build. The gap: content exists, the live operating layer does not. Bionic Lab closes that gap. Once it is live, it becomes the proof piece that changes how the project is perceived externally. Every module after this generates content and distribution. Ship it.
