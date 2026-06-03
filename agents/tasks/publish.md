# Task: Publish

Gated Bionic Banker Agent publisher lane.

## Approval requirement

Publishing is blocked unless Hash explicitly approves the exact class of publish action or an already-approved autopublisher contract covers it.

## Minimum gates

- `npm test` passes from `_astro-source`.
- `npm run build` passes.
- Built output is synced to the root static site when required.
- `git diff --check` passes.
- Public-safety leak scan passes.
- Live URL is verified after merge/deploy.
- Public channel copy is reader-facing, not a build log.

## Forbidden

- No social browser automation.
- No blind scheduled posting.
- No secret values in logs.
- No wallet/trading/compliance authority claims.
