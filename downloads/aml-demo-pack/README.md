# AML Review Engine Demo Pack

This pack supports the Bionic Banker AML Review Engine Lab.

## What is inside

- `sample-input.csv` — small redacted-style sample input shape.
- `sample-output.json` — metrics and sample scored rows from the demo run.
- `risk-memo-sample.md` — analyst-style memo explaining one review scenario.
- `control-map.png` — visual workflow map.
- `limitations.md` — boundaries and non-claims.

## Verification snapshot

- Local tests: 46 passing.
- Demo run version: `v7_blockchain`.
- Demo total transactions: `30`.
- Demo flagged transactions: `30`.
- Risk levels: `{'CRITICAL': 27, 'HIGH': 3, 'MEDIUM': 0}`.

## Control doctrine

The useful output is not only the risk score. The useful output is the control layer around it:

```text
activity → rules → anomaly signals → triage → evidence note → human review
```

No autonomous enforcement or wallet authority is included.
