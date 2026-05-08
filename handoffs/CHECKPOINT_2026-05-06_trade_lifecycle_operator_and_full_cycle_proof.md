# CHECKPOINT_2026-05-06 Trade Lifecycle Operator And Full Cycle Proof

## Objective

Make the Chimera screener -> bundle -> wait -> manage -> close lifecycle understandable, testable, and more productized, with real phase packet outputs, a Lobster workflow, and a replay/improvement loop.

## What Was Completed

- created and mirrored `chimera-trade-lifecycle-operator` skill
- upgraded the trade lifecycle operator guide
- fixed stale local front doors:
  - `scripts/execution_agent.py`
  - `scripts/chimera_entry_exit_sim.py`
- created packet builders:
  - `build_entry_watch_packet.py`
  - `build_active_trade_packet.py`
  - `build_trade_closeout_packet.py`
- created learning sink:
  - `build_lifecycle_learning_queue.py`
- created synthetic full replay:
  - `full_lifecycle_replay.py`
- upgraded `run_chimera_trade_lifecycle_cycle.sh`
- upgraded `build_chimera_lifecycle_context.py`
- upgraded `chimera-trade-lifecycle.lobster`
- mirrored the new logic and docs to:
  - Windows Codex / Claude / OpenClaw skill roots
  - `/root/openclawtrading/scripts`
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`
  - `/root/openclawtrading/workflows/codex`
  - `/root/.openclaw/workspace/workflows/codex`
  - `/root/.openclaw/workspace/orchestration/lobster`
  - `/root/.openclaw/workspace/research/platforms`

## Proof

### Local proof

- `python scripts/test_execution_agent.py`
  - `PASS`
- `python scripts/full_lifecycle_replay.py`
  - `PASS`

### Live VPS proof

- `bash /root/openclawtrading/scripts/run_chimera_trade_lifecycle_cycle.sh`
  - completed
- `python3 /root/openclawtrading/scripts/full_lifecycle_replay.py --output /root/openclawtrading/reports/auto/FULL_LIFECYCLE_REPLAY_PROOF.json`
  - `PASS`

### Key live outputs

- `/root/openclawtrading/reports/auto/ENTRY_WATCH_PACKET_latest.json`
- `/root/openclawtrading/reports/auto/ACTIVE_TRADE_PACKET_latest.json`
- `/root/openclawtrading/reports/auto/TRADE_CLOSEOUT_PACKET_latest.json`
- `/root/openclawtrading/reports/auto/LIFECYCLE_LEARNING_QUEUE.json`
- `/root/openclawtrading/reports/auto/CHIMERA_LIFECYCLE_CONTEXT.json`
- `/root/openclawtrading/reports/auto/FULL_LIFECYCLE_REPLAY_PROOF.json`

## Important Logic Change

Do not force only one artifact to exist.

New rule:

- major packet snapshots can all refresh every cycle for context gathering
- only one phase should be the primary active owner at a time
- `CHIMERA_LIFECYCLE_CONTEXT.json` is the compact ownership truth surface

## Council Findings Captured

Main issues found:

- the lifecycle was still too bundle-centric
- the local execution proof path was broken by stale stubs
- there was no durable learning queue
- there was no single synthetic full-lifecycle replay harness

Applied response:

- packet builders added
- local front doors repaired
- learning queue added
- replay harness added
- Lobster and operator docs tightened

## Still Open

- Task Flow is still not the proven durable symbol-state owner
- there is still no dedicated non-trade thesis-stop review packet
- the strongest full-cycle live proof is still synthetic replay plus live packet generation, not a real market-driven paper trade that progressed through every live phase

## Next Best Step

1. add a `thesis_stop_review` packet for aborted ideas
2. wire Task Flow as the durable symbol lifecycle owner
3. wait for a real paper trade to progress through activation -> management -> closeout
4. use the real closeout to harden `LIFECYCLE_LEARNING_QUEUE.json`
