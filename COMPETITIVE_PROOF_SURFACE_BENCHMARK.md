# Competitive Proof Surface Benchmark

## Purpose

This benchmark guides Bionic Banker toward a sharp AI-agent founder portfolio for finance systems: product-forward, evidence-backed, and understandable to AI+finance-literate readers without becoming a generic compliance brochure.

## Audience lens

Bionic Banker is for recruiters, collaborators, executives, investors, builders, and serious learners who want to understand what Hash is building across AI agents, finance, wallet risk, AML evidence, fraud triage, and human-gated automation.

## Benchmark categories

### 1. AI-agent infrastructure and workflow products

Targets to inspect:

- LangChain / LangGraph
- CrewAI
- AutoGen / Microsoft agent examples
- Replit Agent
- Cognition / Devin
- Anthropic Claude Code positioning
- OpenAI platform examples

What to extract:

- How they explain agents without overclaiming autonomy.
- How they display workflows, tools, traces, and evals.
- How they structure docs versus product pages.
- What trust boundaries they show or hide.
- What a reader can inspect in under 90 seconds.

### 2. RegTech / AML / risk intelligence companies

Targets to inspect:

- Chainalysis
- TRM Labs
- Elliptic
- Sardine
- Unit21
- Alloy
- ComplyAdvantage
- Persona
- Socure

What to extract:

- Risk-scoring language.
- Alert-triage UX patterns.
- Case/evidence packaging.
- Human-review and audit-language patterns.
- How they avoid promising perfect fraud/AML decisions.

### 3. Developer-product proof surfaces

Targets to inspect:

- Vercel
- Linear
- Stripe Docs / Stripe product pages
- Supabase examples
- Retool demos
- PostHog product pages

What to extract:

- Homepage claim compression.
- Navigation model.
- Product/demo split.
- Evidence and case-study cards.
- Visual density without reader overwhelm.

### 4. Founder / builder portfolio sites

Targets to inspect:

- Technical founder personal sites.
- Public AI-builder logs.
- Open-source maintainer portfolios.
- Research-engineer project indexes.

What to extract:

- How scattered work becomes one narrative.
- How projects are ordered.
- How proof artifacts are shown.
- How personal voice and product seriousness coexist.

## Data collection schema

For each site, capture:

- URL:
- Category:
- Primary audience:
- Homepage thesis:
- First 90-second reader path:
- Navigation model:
- Proof/evidence strategy:
- Data/artifact exposure:
- Boundary / risk language:
- Detected frontend stack, if visible:
- What Bionic Banker should copy:
- What Bionic Banker should avoid:
- Specific route/pattern worth adapting:

## Initial hypothesis for Bionic Banker

Bionic Banker should not copy one category. The best target blend is:

- **Founder portfolio clarity** for the homepage.
- **AI-agent infrastructure language** for workflows and Agent Chess.
- **RegTech risk language** for Wallet Risk, AML Status Evidence, and Fraud Alert Triage.
- **Developer-product evidence design** for the evidence catalog and site-health proof QA.

## Current benchmark-driven design decisions

- Homepage should be thesis-first, not archive-first.
- `/projects` should remain system-card oriented.
- `/evidence` should become the reader-facing proof catalog.
- Raw JSON should be secondary, not the first user path.
- `/proof/site-health` should demonstrate proof hygiene and self-auditing.
- Compliance should be a trust boundary, not the whole brand.
