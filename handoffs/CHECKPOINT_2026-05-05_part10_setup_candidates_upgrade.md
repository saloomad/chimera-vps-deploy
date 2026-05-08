# CHECKPOINT - Part 10 setup candidates upgrade

Date: 2026-05-05
Operator: Codex

## Objective

Upgrade `Part 10: Setup Candidates` so it becomes a real ranked multi-path section for Deezoh instead of a flat setup list.

## What changed

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`

Created:

- `agents/deezoh/SETUP_CANDIDATES.md`
- `research/platforms/2026-05-05-setup-candidates-source-matrix.md`
- `research/platforms/2026-05-05-btc-part10-setup-candidates-example.md`

## Part 10 improvements

Added decision-useful fields for:

- current setup-selection context
- ranked setup roles
- setup status by candidate
- explicit opposite-side watch paths
- explicit no-trade preservation
- candidate promotion and demotion rules
- ranking logic that says why one path wins over another

## Owner truth

`Deezoh` is now the owner of Part 10.

It does not invent raw facts.
It converts upstream sections into:

- primary path
- secondary or backup path
- opposite-side watch path
- no-trade path when forcing a setup would be worse

## BTC example verdict

Current BTC Part 10 example now says:

- best directional path is still `reset_long_primary`
- `no_trade_reference` is still the best immediate action
- a deeper long path exists as backup
- the short side is still only an `opposite_watch`

## Why this is better for Deezoh

The section now helps Deezoh compare paths honestly instead of flattening them into one vague idea.

## Remaining work

- continue into Part 11 so the chosen candidate can flow into actual position-handling logic
