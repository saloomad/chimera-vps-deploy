# CHECKPOINT — 2026-05-05 Part 2 Weighting, Replay, Workflow Hardening

## Objective

Finish the Part 2 `Technical Structure` hardening loop so the section is source-owned, Deezoh-useful, replay-gated, and live-proven on the VPS.

## What landed

- repaired Part 2 scoring and selection logic
  - higher timeframe weighting
  - fib ratio and scope weighting
  - stale-source discounting
  - family dedupe
  - touch bonus
- repaired resistance selection
  - reclaimed-below-price zones no longer show up as overhead resistance
  - actionable resistance selection now favors meaningful overhead zones instead of blind raw-score winners
- repaired top-level readiness signaling
  - local no-chart runs now show chart-proof limitations honestly
  - live VPS runs now show `ready_for_final_trade_guidance` only when Jackson proof is live
- replay harness now has:
  - explicit regression budget
  - pass / iterate verdict
  - outcome breakdowns
  - changed / losing window examples
- updated reusable workflow + skill + owner docs

## Proof

### Local

- `TECHNICAL_STRUCTURE_latest.json` rebuilt successfully
- `TECHNICAL_STRUCTURE_BACKTEST_latest.json` verdict: `pass`
- metrics:
  - support delta: `+0.010`
  - resistance delta: `-0.036`
  - combined delta: `-0.014`

### VPS

- synced patched files to:
  - `/root/openclawtrading/...`
  - `/root/.openclaw/workspace/...`
  - `/root/.openclaw/kimi-skills/...`
- re-ran live chart analyzer on VPS
- re-ran VPS replay
- live chart proof:
  - target ready: `true`
  - cdp port: `9333`
  - symbol: `BINANCE:BTCUSDT`
  - resolution: `240`
- VPS report:
  - `freshness_state = fresh`
  - `readiness_state = ready_for_final_trade_guidance`
- VPS replay verdict: `pass`
- VPS replay metrics matched local

## Files changed in this slice

- `scripts/build_technical_structure_report.py`
- `scripts/backtest_technical_structure_section.py`
- `scripts/technical_structure_probe.py`
- `agents/chart-analyzer/AGENTS.md`
- `agents/chart-analyzer/TOOLS.md`
- `agents/indicator-analyst/AGENTS.md`
- `agents/indicator-analyst/TOOLS.md`
- `workflows/codex/chimera-bundle-section-proof-and-hardening-loop.md`
- `skills/chimera-bundle-section-proof-and-hardening/SKILL.md`

## Remaining open work

- Part 3 still needs its own canonical replay/historical-proof harness
- the next bundle sections should now follow this same workflow instead of inventing their own proof shape
- optional later polish:
  - improve critical-marker labels beyond generic swing/key-level wording

## Resume point

Next meaningful continuation:

1. push the relevant shared files
2. use the same proof-and-hardening loop on the next section
3. for Part 3 specifically, build the canonical replay owner/harness before claiming parity with Part 2

