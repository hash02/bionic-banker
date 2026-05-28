# Bionic Banker Public Proof Contract

## Purpose

Bionic Banker is Hash's public evidence surface for agentic finance work: AI-agent systems, wallet-risk reasoning, AML/compliance evidence, fraud-triage workflows, and human-gated automation.

The site should be understandable to any AI-and-finance-literate reader: recruiters, collaborators, executives, investors, builders, and serious learners. It should feel like a sharp AI-agent founder portfolio, not a generic compliance brochure.

## Audience and style

- **Primary audience:** people who can understand or want to understand AI + finance systems.
- **Secondary audience:** recruiters, collaborators, executives, investors, and technically curious readers.
- **Tone:** product-forward, founder-sharp, evidence-backed.
- **Compliance posture:** visible trust boundary, not the entire personality.
- **Default promise:** inspectable public proof, not production authority.

## Flagship reading order

1. Wallet Risk Assessment — shows risk judgment and reviewer-facing explanation.
2. AML Status Evidence — shows audit boundary and evidence packaging.
3. Fraud Alert Triage — shows regulated workflow packaging with synthetic data.
4. Agent Chess / Agent Workflow — shows agent work that requires human review.
5. Site Health / Proof QA — shows the public proof surface audits itself.

## Metric contract

Every public count must use one label and one source.

- **Public system cards**
  - Source: cards in `_astro-source/src/pages/projects.astro`.
  - Meaning: rendered public-facing system/project cards.
  - Current value: 11.

- **Evidence catalog sections**
  - Source: `projects.length` in `_astro-source/public/dashboard-data/public-proof-catalog.json`.
  - Meaning: public proof-catalog entries used for evidence rows and guided evidence surfaces.
  - Current value: 8.

- **Catalog evidence sources**
  - Source: sum of `sources.length` across public proof catalog projects.
  - Meaning: supporting source links attached to catalog evidence lanes.
  - Current value: 21.

- **Catalog boundaries**
  - Source: sum of `limits.length` across public proof catalog projects.
  - Meaning: explicit public boundaries / stated limits in evidence lanes.
  - Current value: 36.

- **Articles**
  - Source: markdown files in `_astro-source/src/content/blog/*.md`.
  - Meaning: source articles in the content collection.
  - Current value: computed at build/check time.

## Label rules

Do not use these words interchangeably:

- `system cards` are not `evidence lanes`.
- `projects` are not automatically `proof records`.
- `sources` are not `articles`.
- `boundaries` are not the same thing as `limits named` unless the page explicitly says the source.

Preferred public labels:

- Public system cards
- Evidence catalog sections
- Catalog evidence sources
- Catalog boundaries
- Articles
- Number notes
- Stated limits / boundaries
- View system
- Open evidence page
- Raw JSON

Avoid primary labels such as:

- Systems, when the count is actually catalog lanes.
- Areas, when the count is actually catalog lanes.
- Evidence records, when the link is raw JSON and a rendered evidence page exists.

## Page contract

Every major proof page should answer:

1. What is this?
2. What can a reader inspect?
3. What evidence supports it?
4. What is explicitly not claimed?
5. Where should the reader go next?

Required public proof components:

- A clear claim.
- Evidence or source links.
- Boundary language.
- Human-gated or public-safe framing when relevant.
- A next route.

## Claim levels

Use these levels deliberately:

- **Working artifact:** a functioning page, repo, JSON, note, or demo surface exists.
- **Public proof:** the artifact is public-safe and evidence-backed.
- **Portfolio-grade:** safe to show as evidence of shipped work and judgment.
- **Commercial-grade:** only after accessibility, security, performance, legal/copy, monitoring, and production-readiness review.

Do not call something commercial-grade just because it looks polished.

## Public-safety boundaries

Banned or high-review claims:

- autonomous compliance approval
- live trading authority
- execution authority
- guaranteed fraud detection
- guaranteed AML correctness
- production-ready compliance system
- private prompts, private paths, wallet secrets, API keys, tokens, internal hostnames, raw logs

Preferred boundary language:

- human approval required
- public-safe evidence sample
- synthetic data where applicable
- no filing, trading, deployment, wallet, or enforcement authority
- reviewer-ready, not self-executing

## Engineering rule

If a screenshot shows confusion, do not patch only the sentence. Add or improve a deterministic check so the same class of drift is caught before publication.
