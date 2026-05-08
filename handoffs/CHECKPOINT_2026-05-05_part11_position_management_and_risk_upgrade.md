# CHECKPOINT - Part 11 position management and risk upgrade

Date: 2026-05-05
Operator: Codex

## Objective

Upgrade `Part 11: Position Management And Risk` so it becomes a real handling section instead of a thin placeholder.

## What changed

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`

Created:

- `agents/position-sizer/AGENTS.md`
- `agents/position-sizer/TOOLS.md`
- `research/platforms/2026-05-05-position-management-and-risk-source-matrix.md`
- `research/platforms/2026-05-05-btc-part11-position-management-and-risk-example.md`

## Part 11 improvements

Added decision-useful fields for:

- management posture
- entry timing rule
- do-not-chase rule
- add conditions
- stop tightening rule
- reduce plan
- break-even rule
- symbol exposure conflict rule
- abort-before-entry rule
- management fail conditions

## Owner truth

`position-sizer` is now the owner of Part 11.

It does not invent the thesis.
It translates the chosen candidate from Part 10 into a handling plan that `execution` can consume later.

## BTC example verdict

Current BTC Part 11 example now says:

- chosen setup is `reset_long_primary`
- current management posture is still `paper_watch_only`
- no chase is allowed
- same-symbol backup paths cannot be treated like separate full-risk trades

## Why this is better for Deezoh

The section now separates:

- good idea
- good candidate
- good handling plan

instead of pretending those are the same thing.

## Remaining work

- no section-specific blocker remains; the broader bundle objective was closed later by the full BTC end-to-end consumer proof
