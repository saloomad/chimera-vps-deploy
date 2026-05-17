---
name: chimera-lifecycle-review-council
description: Project-specific council skill for reviewing the Chimera screener to bundle to entry-watch to active-trade lifecycle. Use when the problem is in the trade-document flow, phase promotion, Deezoh reasoning, no-trade preservation, or lifecycle causality.
---

# Chimera Lifecycle Review Council

Use this when the target is the current Chimera trade-document and lifecycle stack, not generic debugging.

This skill is for questions like:

- why did the screener promote this coin
- why is the bundle focused on this symbol
- why did entry-watch or active-trade progress too early
- why did no-trade lose or survive
- what phase transition was wrong
- what document failed to explain the decision
- what should be improved in the bundle, workflow, or Deezoh reasoning

## Read First

1. `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
2. `C:\Users\becke\.codex\skills\review-debug-simulation-orchestrator\SKILL.md`
3. `C:\Users\becke\.codex\skills\chimera-review-debug-orchestrator\SKILL.md`
4. `references/PHASE_REVIEW_RUBRIC.md`
5. `references/TRANSITION_DEBUG_CHECKLIST.md`
6. `references/LIVE_VS_REPLAY_PROOF_ORDER.md`

## Council-First Rule

Start with reasoning review or council critique before deterministic checks when the main question is:

- was the decision good
- what did the system miss
- which stronger alternative was ignored
- why does this feel wrong even when the packets exist

Use deterministic checks after that to confirm or narrow the suspected fault.

## Default Council Shape

Use this default council unless the target needs fewer roles:

- `reviewer`
  - explains what most likely went wrong
- `skeptic`
  - argues for the strongest alternative interpretation
- `builder`
  - proposes the smallest high-value fix

Default artifact sinks:

- `trace/review-debug/chimera-lifecycle/` for transcripts
- `research/platforms/` for the durable review note
- `chimera-vps-deploy/handoffs/` when the result changes the active continuation path

Preferred run shape for repeatable scenario work:

- keep the scenario itself under:
  - `trading_system/scripts/labs/fixtures/chimera_scenario_packs/`
- build prompt packs with:
  - `python C:\Users\becke\claudecowork\scripts\build_chimera_council_case.py --mode prompt-pack --scenario <scenario-json>`
- keep each saved council run under:
  - `trace/review-debug/chimera-lifecycle/<scenario-name>/<timestamp>/`
- minimum files:
  - `transcript.md`
  - `verdict.json`
  - `scorecard.json`

After adding or fixing a saved run, verify family coverage with:

- `python C:\Users\becke\claudecowork\scripts\run_chimera_council_trace_coverage.py`

If no real council transcripts or equivalent outputs exist, label the result as a lightweight review, not a full council run.

## Phase Questions

Review the lifecycle in order:

1. `screener`
   - why was this symbol selected or deferred
   - what stronger alternative existed
2. `research bundle`
   - did the bundle explain the symbol focus and the main risks clearly
3. `entry watch`
   - did the system wait for the right trigger and confirmation
4. `active trade`
   - if activated, was that promotion justified
5. `closeout or thesis stop`
   - did the outcome review honestly say whether earlier promotions were right

## Required Outputs

Every run should leave:

- one lifecycle phase under review
- one strongest alternative path
- one decision-causality summary
- one first bad transition, if any
- one patch-first recommendation
- one still-unproven note

## Default Red-Team Focus

Always consider:

- no-trade should win
- stale helper data misleads a promotion
- screener top pick conflicts with current focus
- illegal phase jump
- wrong symbol or wrong side still wins

## Closeout Standard

Do not close the review with only "passed" or "failed."

Say:

- what phase was strongest
- what phase was weakest
- what most likely caused the miss
- what smallest fix should land first
