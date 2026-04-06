# TASK: Rebuild Infographics for agentic-ai-banking post

## Context
Maya sent 4 infographic HTML files to blog-visuals/agentic-ai-banking/. 
They have WRONG colors (blue, red, purple). They need to be rebuilt from scratch 
using the correct bionicbanker.tech palette: GREEN, BLACK, WHITE ONLY.

## Reference
Look at the previous post's infographics for style reference:
- blog-visuals/ai-agent-gap.png (the hero image from Series 1)
- The CSS data-viz system from the ai-agent-gap.md post (callout-stat, stat-row, stat-card classes)
- Site palette: #020204 bg, #1fa068 green, #e4e4ec text, #080810 card bg

## What to rebuild (4 infographics, all GREEN/BLACK/WHITE only):

### 01-hero-banner.html (1200x630px)
Title: "The Agentic Gap" Subtitle: "How the World's Banks Are Deploying AI Agents"
4 countries (US, India, Australia, Canada) race/progression visual
bionicbanker.tech branding footer

### 02-global-stats.html (1200x630px) 
Command-center dashboard:
- $50B global market spend (KPMG 2025)
- 600% increase in finance team adoption
- 70% of leaders deploying/exploring agents
- $2.6T-$4.4T annual value potential  
- 99% plan agents, only 11% in production

### 03-country-comparison.html (1200x630px)
4-column comparison:
- US (JPMorgan): 360K hrs saved, 500+ AI use cases, $1.5B target, 95% AML reduction
- India (HDFC): 0.4s response, 127K+ VLEs, millions of queries, instant loans
- Australia (ANZ): 20 platforms to 1, ~1 month/year saved, first APAC at scale
- Canada (Big 5): RBC #3 global, 1.2M hrs saved (CIBC Q1), 90% email auto (Scotia), $1B target (RBC)

### 04-canada-big5.html (1200x630px)
Canada Big 5 deep dive:
- RBC: #3 global, 50 companies/analyst (was 15), $1B target, 27K Assist users
- TD: #13 global, >20% score increase YoY
- Scotiabank: 90% autonomous email, 70% staff redeployed, since 2018
- CIBC: 1.2M hours Q1 2026, 30K users, 44% conversion lift, Best GenAI award
- BMO: Rising talent development

## Rules
- GREEN (#1fa068), BLACK (#020204), WHITE (#e4e4ec) ONLY. No blue. No red. No purple.
- Match the style of existing bionicbanker infographics
- Self-contained HTML (inline CSS, inline fonts from Google)
- Generate PNG exports (1200x630, 2x retina if possible)
- After rebuilding, run astro build and git push

## After infographics
- The blog post markdown is already at: _astro-source/src/content/blog/agentic-ai-banking.md
- LinkedIn drafts are at: drafts/agentic-ai-banking-linkedin-series2.md and drafts/agentic-ai-banking-linkedin-article-series2.md
- Build site with npm run build, copy dist, git push

