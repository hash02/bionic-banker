# AML Risk Memo Sample

## Scenario

A sample review queue contains transactions with mixer-touch, high-risk-jurisdiction, burst, and large-amount indicators.

## Local demo metrics

- Total transactions reviewed: 30
- Flagged transactions: 30
- Flag rate: 100.0%
- Risk levels: {'CRITICAL': 27, 'HIGH': 3, 'MEDIUM': 0}

## Analyst interpretation

The engine should be treated as a triage assistant. It can highlight rows that deserve review, explain the rules that fired, and preserve a source/evidence note. It should not decide intent, identity, enforcement action, account closure, SAR filing, or customer outcome.

## Human review questions

1. Which source record supports each rule hit?
2. Is the wallet/entity context complete enough to escalate?
3. Is the alert caused by a known benign pattern?
4. What evidence is missing?
5. What is the next allowed action under policy?

## Decision boundary

Escalate for human review. Do not treat the score as a final verdict.
