# CHECKPOINT - Part 9 risk and invalidation upgrade

Date: 2026-05-05
Operator: Codex

## Objective

Upgrade `Part 9: Risk And Invalidation` so it becomes a real pre-entry thesis-risk section for Deezoh instead of a stub.

## What changed

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `agents/risk-engine/AGENTS.md`

Created:

- `agents/risk-engine/TOOLS.md`
- `research/platforms/2026-05-05-risk-and-invalidation-source-matrix.md`
- `research/platforms/2026-05-05-btc-part9-risk-and-invalidation-example.md`

## Part 9 improvements

Added decision-useful fields for:

- noise versus real invalidation
- why the thesis is still alive
- what still has to hold
- active risks now
- thesis breakers
- invalidation ladder
- downgrade-to-wait logic
- full invalidation logic
- opposite-bias flip logic
- what the opposite case is still missing
- stale or proxy lanes that limit confidence
- missing confirmation before conviction
- no-trade triggers

## Owner truth

`risk-engine` is now the owner of Part 9.

It does not fetch raw facts.
It synthesizes risk and invalidation from:

- Part 2 structure
- Part 3 indicators
- Part 4 derivatives
- Part 5 liquidation
- Part 6 macro
- Part 7 catalysts
- Part 8 structural / market intel

## BTC example verdict

Current BTC Part 9 example now says:

- thesis under review is still `reset-long`, not immediate short
- main active risk is bad timing, not full thesis failure yet
- short-term weakness is still noise unless it spreads into 4h damage
- the short case becomes real only if weakness spreads upward and participation turns against the upside

## Why this is better for Deezoh

The section now tells Deezoh:

- what to ignore
- what to respect
- what forces wait
- what forces no-trade
- what would start making the other side real

It now also has a detailed walkthrough file:

- `research/platforms/2026-05-05-btc-part9-risk-and-invalidation-explained.md`

## Remaining work

- fold Parts 6 through 8 into a fully filled Part 9 example so the broader veto lanes are not still marked incomplete
- test how Deezoh consumes Part 9 inside a full bundle, not only as a standalone section
