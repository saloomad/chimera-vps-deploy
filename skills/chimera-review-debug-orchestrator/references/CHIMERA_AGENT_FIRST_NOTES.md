# Chimera Agent-First Notes

Use agent reasoning before scripts when:

- Deezoh seems to reach the wrong posture
- the symbol choice feels inconsistent
- the same output "passes" but still looks wrong to a trader
- a user is asking what was missed
- you need a council to compare long, short, and no-trade honestly

Use scripts first when:

- you are checking fields, files, paths, schemas, or invariants
- you need a repeatable replay
- you need a machine-readable regression result

Healthy split:

- agents:
  - critique
  - counterexamples
  - missed questions
  - failure scenarios
  - fix prioritization

- scripts:
  - fixtures
  - replay
  - scoring helpers
  - contract validation
  - report generation

Bad pattern:

- a script says pass
- no one checks whether the decision was still weak

Better pattern:

1. agent or council finds the likely weak point
2. script proves or disproves it repeatably
3. learning loop captures the fix if it matters beyond the session
