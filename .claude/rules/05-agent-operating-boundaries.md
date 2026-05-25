# Agent Operating Boundaries

This repo can be edited by AI coding agents, but the public site must stay safe and inspectable.

## Agent behavior

Agents should:

- orient with `git status --short --branch`
- read `AGENTS.md`, `CLAUDE.md`, and relevant `.claude/rules/*.md`
- edit the smallest source area that satisfies the task
- run deterministic checks before claiming success
- keep scratch notes, QA artifacts, and handoff files unstaged unless requested
- summarize changed files, checks, and remaining risks

Agents must not:

- read or expose secrets
- publish private prompts, local paths, hostnames, raw logs, or internal agent transcripts
- change production/DNS/Cloudflare/newsletter/analytics settings unless Hash explicitly asks
- force-push
- claim commercial-grade readiness without dedicated accessibility, performance, mobile, legal/copy, and monitoring checks
- convert human-gated workflows into autonomous external action

## Claude Code usage notes

For one-shot edits, prefer print mode with bounded tools and turns, for example:

```bash
claude -p "Fix the theme guard for blue/cyan accents and run the targeted checker" --allowedTools "Read,Edit,Bash(npm run test:opportunity-engine)" --max-turns 8
```

For multi-turn work, use a named tmux session or Claude worktree, then clean it up. Keep worktree changes isolated from the main checkout.

## What to learn from this structure

The `.claude/` folder is not application code. It is the operating manual for coding agents. It should make the repo safer by telling agents:

- where truth lives
- what not to touch
- what commands prove a change
- what design/copy constraints are locked
- what public-safety boundaries cannot be crossed

Good agent context reduces repeated explanation, accidental broad edits, and hallucinated release claims.
