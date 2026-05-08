# CHECKPOINT_2026-05-06 Universal Review Debug Orchestration And Lifecycle State

## Objective

Finish the open lifecycle hardening work by adding one universal review/debug skill, a thesis-stop review path, better lifecycle state surfaces, and live proof on the real VPS.

## Completed Work

- created `chimera-review-debug-orchestrator` as the new universal coordinator skill
- mirrored that skill to:
  - Windows Codex
  - Windows Claude
  - Windows OpenClaw
  - shared repo skills
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`
- created `CHIMERA_THESIS_STOP_REVIEW_TEMPLATE.md`
- created:
  - `scripts/build_thesis_stop_review_packet.py`
  - `scripts/build_symbol_lifecycle_state.py`
  - `scripts/run_chimera_review_debug_orchestration.py`
- upgraded:
  - `scripts/run_chimera_trade_lifecycle_cycle.sh`
  - `scripts/build_chimera_lifecycle_context.py`
  - `orchestration/taskflow.json`
  - `workflows/codex/chimera-screener-to-trade-document-flow.md`
  - `research/platforms/2026-05-06-chimera-trade-lifecycle-operator-guide.md`
  - `chimera-vps-deploy/skills/chimera-trade-lifecycle-operator/SKILL.md`

## Key Logic Changes

- lifecycle flow now includes a thesis-stop review branch for good non-trades
- lifecycle context now exposes top-level aliases like:
  - `primary_phase`
  - `focus_symbol`
  - `active_owner`
  - `active_trade_state`
  - `closeout_state`
  - `thesis_stop_state`
- symbol lifecycle state now exposes:
  - `primary_phase`
  - `active_owner`
  - `source_cycle_mode`
  - `packet_chain`
- review/debug runner now checks:
  - Task Flow alignment
  - lifecycle packet existence
  - lifecycle alias completeness
  - phase-chain completeness
  - replay proof
- review/debug runner now skips packet checks on a non-populated local report surface instead of treating that as a runtime failure

## Proof

### Local proof

- `python scripts/full_lifecycle_replay.py --output reports/auto/FULL_LIFECYCLE_REPLAY_PROOF_local.json`
  - `PASS`
- `python scripts/run_chimera_review_debug_orchestration.py --reports-dir reports/auto --output reports/auto/CHIMERA_REVIEW_DEBUG_REPORT_local.json`
  - `PASS`
  - local lifecycle packet checks correctly marked `skipped` because the local report surface is not the populated live lifecycle truth

### Live VPS proof

- `python3 -m py_compile` on new lifecycle/review scripts
  - `PASS`
- `bash /root/openclawtrading/scripts/run_chimera_trade_lifecycle_cycle.sh`
  - completed
- `python3 /root/openclawtrading/scripts/run_chimera_review_debug_orchestration.py --reports-dir /root/openclawtrading/reports/auto --output /root/openclawtrading/reports/auto/CHIMERA_REVIEW_DEBUG_REPORT.json`
  - `PASS`

### Important live outputs

- `/root/openclawtrading/reports/auto/THESIS_STOP_REVIEW_PACKET_latest.json`
- `/root/openclawtrading/reports/auto/SYMBOL_LIFECYCLE_STATE.json`
- `/root/openclawtrading/reports/auto/CHIMERA_LIFECYCLE_CONTEXT.json`
- `/root/openclawtrading/reports/auto/CHIMERA_REVIEW_DEBUG_REPORT.json`

### Current live state from proof run

- `primary_phase: entry_watch`
- `focus_symbol: SOLUSDT`
- `active_owner: entry-watch`
- `source_cycle_mode: range_rotation`
- `thesis_stop_state: not_applicable`

## Decisions Made

- do not replace all existing proof/backtest/replay skills; route through them with one coordinator skill
- treat local missing lifecycle packet outputs as a surface-selection issue, not an automatic system failure
- keep thesis-stop review as an auxiliary branch, not a forced primary phase

## Still Open

- a naturally progressing live paper trade through activation -> management -> closeout still has not happened yet
- Task Flow now points at the correct lifecycle flow and state surface, but the stronger proof is still report-driven ownership rather than a fully separate dedicated Task Flow worker

## Next Best Step

1. wait for a real paper trade to reach activation and closeout
2. use that closeout to harden the learning queue and review/debug recommendations
3. if needed, promote Task Flow from configured state surface to a stronger dedicated runtime owner
