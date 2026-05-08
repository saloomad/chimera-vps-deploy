# CHECKPOINT - 2026-05-06 Part 11 Owner Wiring Heartbeat

## What moved in this heartbeat

- resumed from the latest screener/Deezoh checkpoint instead of restarting
- checked the next unresolved gap after the screener proof slice
- confirmed `Part 11: Execution Plan, Orders, And Risk` already exists in the bundle template, but the live owner/consumer wiring still needed tightening
- updated:
  - `agents/entry-watch/AGENTS.md`
  - `agents/trade-judge/AGENTS.md`

## Why this matters

The Part 11 contract is not only a template section.

This pass made the live consumers more explicit:

- `entry-watch` now states that it must read and obey the `trigger_contract`, `execution_readiness`, `do_not_chase_rule`, `order_plan`, and abort conditions from Part 11 instead of improvising
- `trade-judge` now explicitly reads the bundle tail and must treat `wait_for_reset`, `wait_for_trigger`, and `no_entry` as real blockers to execution-ready posture

## Live mirror proof

Mirrored to the real VPS surfaces:

- `/root/openclawtrading/agents/trade-judge/AGENTS.md`
- `/root/.openclaw/workspace/agents/trade-judge/AGENTS.md`
- `/root/.openclaw/workspace/agents/entry-watch/AGENTS.md`
- `/root/.openclaw/workspace/agents/spawned/entry-watch/AGENTS.md`

## Still open

- Part 11 still needs a full worked example / proof pass, not just owner wiring
- Part 12 and the bundle-tail closeout are still open
