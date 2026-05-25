# Layer 3 living field map goals

> **For Hermes:** Use this as the north star for Bionic Banker Layer 3 work. Build in small verified slices. Do not bury the reader under proof language. Make the site feel like an operating system someone can enter.

**Goal:** Turn Bionic Banker from a proof-heavy portfolio into a living public field map for AI, finance risk, agents, markets, and learning.

**Architecture:** The homepage is the map. Apps are clickable systems. Signals are the live pulse. AI Intelligence explains the agent and technology world. Blog keeps the learning loop alive. Proof and evidence stay available, but they stop dominating the front door.

**Tech Stack:** Astro static site, committed root output, deterministic Node checkers, public-safe JSON, mobile QA.

---

## Critical stance

Hash's direction is better than the previous proof-only framing. The proof spine was needed first because public claims needed boundaries. Now the site needs life, navigation, and a reason to return.

This is not flattery. The direction is stronger because it solves a real reader problem: a cold visitor needs a simple route through a complex body of work.

## Audience

- Recruiters who understand AI and finance.
- Collaborators who want to inspect judgment.
- Younger readers who learn through apps, maps, and visual systems.
- Builders who want to understand agents, compliance, wallets, and markets.
- Hash himself, so the site becomes a learning and publishing loop.

## Public navigation target

1. **Start Quest**: a first-reader path.
2. **Apps**: usable systems and demos with boundaries.
3. **Signals**: market, agent, and risk pulse.
4. **AI Intelligence**: agent stack, tooling, research, and technology watchlist.
5. **Blog**: field notes and learning posts.
6. **About**: Hash, voice, work, collaboration.

Proof routes remain available in the footer and inside cards. They are trust infrastructure, not the main personality.

## Voice rules

- Fewer words. More meaning.
- No long dash glyphs.
- No arrow glyphs in public copy.
- No fake hype.
- No trading or compliance authority claims.
- Use black, white, and green. Depth comes from green-tinted black and soft white, not grey.

Example target voice:

> AI, finance, and the world ahead.
> Bionic Banker follows how technology is changing money, risk, work, and the systems people trust.

## Visual direction

Best mix:

- NVIDIA: black and green authority.
- Spotify: alive, app-like dark surface.
- Vercel: clean navigation and simple cards.

Avoid:

- Childish game badges.
- Random 3D decoration.
- Retail trading dashboard energy.
- Grey corporate deadness.

## Build sequence

### Slice 1: Field-map spine

- Simplify global nav.
- Add Apps route.
- Add Signals route.
- Add AI Intelligence route.
- Rename Articles to Blog in public navigation.
- Add deterministic checker for the new route labels and no arrow glyphs on the main public shell.

### Slice 2: Apps surface

- Make Apps the public catalog for clickable systems.
- Keep each card focused on what it does, what it proves, and what it cannot do.
- Add stronger entry points for Wallet Risk, AML Status Evidence, Fraud Alert Triage, Agent Chess, and Site Health.

### Slice 3: Signals board

- Keep homepage to a small live pulse.
- Put full market and agent activity on Signals.
- Add public API widgets only with clear “not investment advice” framing.

### Slice 4: AI Intelligence learning loop

- Create a page that tracks agents, tools, model shifts, and infrastructure patterns.
- Turn new technology discoveries into blog candidates.
- Use public-safe images for tools and concepts where allowed.

### Slice 5: 3D relevance layer

- Add one high-quality 3D or animated map element after the information architecture is stable.
- It must explain the site. It cannot be decoration only.
- If it hurts mobile or clarity, remove it.

## Verification gate

Before shipping each slice:

- `npm run qa:proof`
- `npm test`
- `npm run qa:mobile`
- `npm run build`
- sync `dist` to root output
- run checker again
- inspect local pages in browser
- scan changed public files for private data and unsafe claims
