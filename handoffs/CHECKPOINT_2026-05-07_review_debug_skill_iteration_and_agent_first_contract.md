# CHECKPOINT_2026-05-07 Review Debug Skill Iteration And Agent-First Contract

## Objective

Turn the review/debug lesson from recent Chimera work into a reusable system:

- make the review/debug/simulation lane work for general use, not just one trading case
- add a project-specific Chimera lifecycle review skill
- reduce script-overuse by forcing agent-first diagnosis where that is the honest route

## Completed Work

- created universal skill:
  - `C:\Users\becke\.codex\skills\review-debug-simulation-orchestrator`
- upgraded Chimera adapter skill:
  - `C:\Users\becke\.codex\skills\chimera-review-debug-orchestrator`
- created task-specific skill:
  - `C:\Users\becke\.codex\skills\chimera-lifecycle-review-council`
- tightened lower proof-lane skills:
  - `pipeline-simulation-lab`
  - `openclaw-replay-and-backtest`
- added new contract/reference files:
  - universal output contract
  - default red-team pack
  - Chimera route overrides
  - Chimera red-team cases
  - Chimera A/B judging notes
  - Chimera debug verdict template
  - lifecycle phase-review and transition-debug references
- validated all five skill folders with `quick_validate.py`
- mirrored all five skills to:
  - `C:\Users\becke\.claude\skills`
  - `C:\Users\becke\.openclaw\skills`
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills`
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`

## Council Findings That Landed

Main issues found by the council:

- the first version still routed better than it debugged
- "agent-first" needed a real evidence contract
- replay needed a first-divergence protocol
- the Chimera adapter needed more explicit route overrides and adversarial cases
- the system needed one task-specific skill for the screener-to-trade lifecycle itself

Those are now encoded directly in the skills.

Final recheck result:

- one last high-priority gap remained after the first patch round:
  - `agent-first` was still not operationally easier than script fallback
- that was fixed by adding:
  - canonical real agent-run path to the universal skill
  - canonical Chimera agent-run path to the Chimera adapter
  - default council shape and artifact sinks to the lifecycle review skill

## Live / Tooling Proof

Confirmed:

- all five source-of-truth skill folders validate with `quick_validate.py`
- the new and updated skills were mirrored to the real Windows and VPS skill roots

Important tooling boundary:

- the `plugin-eval` skill documentation exists locally
- the `plugin-eval` executable is not currently callable on PATH
- that means local plugin-eval benchmarking is still a tooling gap, not a finished proof lane

## Remaining Project Work

1. build the first real scenario packs for the Chimera failure families:
   - no-trade should win
   - illegal phase promotion
   - stale helper misleads decision
   - wrong symbol or side promotion
2. add a real agent-run harness so behavior proof is not limited to prompt/scoring approximations
3. add lifecycle invariant checks for illegal phase transitions
4. decide whether to make `plugin-eval` callable locally or keep using the current local-first validation stack

## Main Decision

Do not remove scripts.

Instead:

- keep scripts for deterministic proof, replay, validation, and regression protection
- require agent reasoning first for open-ended diagnosis, critique, and scenario review
- make the skills say exactly which kind of evidence came from reasoning and which came from deterministic checks
