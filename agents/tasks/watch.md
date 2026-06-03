# Task: Watch

Read-only Bionic Banker Agent watcher.

## Inputs

- local source tree;
- optional `BIONIC_BASE_URL` environment variable, default `https://bionicbanker.tech`.

## Allowed checks

- critical route reachability;
- local article count from `_astro-source/src/content/blog/*.md`;
- existence of root agent contract;
- public-safety leak script status;
- optional connector presence by environment variable name only.

## Forbidden actions

- no file mutation except a caller-approved report path;
- no deploy;
- no social post;
- no wallet, trade, KYC, SAR, or compliance filing action;
- no secret value output.

## Output

A JSON health report or Markdown summary with status, checked facts, missing context, clear limits, and next human question.
