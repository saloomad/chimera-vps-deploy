---
name: chimera-hybrid-scenario-lab
description: Run Chimera and Deezoh through a hybrid scenario matrix that combines deterministic script checks with agent reasoning. Use when you need to test market conditions, setup choice logic, follow-up questions, lifecycle progression, closeout behavior, and whether the system learns instead of only passing contracts.
---

# Chimera Hybrid Scenario Lab

Use this skill when the question is:

- did we test enough market conditions
- does Deezoh choose the right workflow, setup, and no-trade path
- does Deezoh ask for more data when the evidence is stale, contradictory, or incomplete
- does the lifecycle progress logically from screener to closeout
- does the system learn from results
- how do we speed up trade closeout testing without waiting for a natural paper trade

## Read First

1. `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
2. `C:\Users\becke\.codex\skills\objective-orchestration-loop\SKILL.md`
3. `C:\Users\becke\.codex\skills\chimera-review-debug-orchestrator\SKILL.md`
4. `C:\Users\becke\.codex\skills\chimera-bundle-consumer-simulation\SKILL.md`
5. `C:\Users\becke\claudecowork\workflows\codex\deezoh-market-condition-and-trade-lifecycle-loop.md`
6. `C:\Users\becke\claudecowork\scripts\run_hybrid_market_condition_scenario_matrix.py`
7. `C:\Users\becke\claudecowork\scripts\tests\current_focus_full_lifecycle_smoke.py`

## Non-Negotiable Rule

Never stop at scripts only.

This skill is hybrid by definition:

- scripts prove contracts, workflow routing, lifecycle state, and reproducible scenario behavior
- agent reasoning judges whether:
  - the winning setup really should have won
  - the strongest rejected alternative lost for the right reason
  - Deezoh asked the most decision-changing next question
  - more data should have been requested before promotion
  - the learning artifacts captured something useful

## Default Scenario Families

At minimum, test:

1. `data_unreliable`
2. `event_control`
3. `trend_auction`
4. `range_auction`
5. `transition_or_exhaustion`
6. `liquidity_trap`
7. `active_trade_management`
8. `wrong_symbol_or_wrong_side_risk`
9. `no_trade_should_win`

## Required Deterministic Lane

Run:

- `python scripts/run_hybrid_market_condition_scenario_matrix.py`
- `python scripts/build_synthetic_natural_comparison_review.py`

Do not stop at `status` only.

The synthetic-vs-natural comparison artifact must also expose:

- `follow_through_signal.owner_should_act_next`
- `follow_through_signal.action_state`
- `follow_through_signal.priority`
- whether the current case should block a falsely-green review
- whether the case is only `fresh_watch`, is already `aging_watch`, or has become `stale_watch`

When lifecycle closeout matters, also run:

- `python scripts/tests/current_focus_full_lifecycle_smoke.py`

When live bundle readiness matters, also run:

- `bash /root/openclawtrading/scripts/run_research_bundle_refresh.sh`

## Required Agent Review

After the scripts run, do not just paste PASS/FAIL.

Write an agent review that answers:

- what market condition was this really
- was the chosen workflow logical
- should Deezoh have asked another specialist first
- what missing question would most improve the decision
- what weakest instruction or source order caused the miss
- what should be changed before trusting this scenario more

This must be a real review artifact, not only same-thread commentary.

Minimum review shape:

- one reviewer verdict
- one skeptic or challenger verdict
- one builder recommendation with the smallest next fix
- one saved artifact such as `HYBRID_SCENARIO_AGENT_REVIEW.json`

That artifact should be fresh for the current run, not a recycled old note.

Minimum current-run tie fields:

- `review_target.scenario_count`
- `review_target.covered_families`
- `review_target.fast_closeout_smoke_ok`
- `review_target.outcome_matrix_ok`

Symbol-choice proof is also required when more than one candidate is in play:

- the matrix should show which symbol actually stayed in focus
- the matrix should show whether that symbol was the raw top-ranked name or a cleaner second-choice
- the review should say whether the focus stayed on the right symbol for the right reason
- test both directions:
  - when a cleaner second-choice should beat the favorite
  - when the favorite should correctly stay in focus

If the review artifact is old or not tied to the current deterministic scope, do not call the result full hybrid proof.

If that artifact does not exist, call the run:

- `preflight`
- or `deterministic-only proof`

Do not call it full hybrid proof.

## What This Skill Must Produce

Every run should leave:

- one scenario matrix artifact
- one synthetic-vs-natural comparison artifact
- one lifecycle or closeout proof when relevant
- one agent-written review of the matrix
- one gap list
- one improvement owner list
- one durable note or checkpoint if the contract changed

## Good Closeout

The run is only good if it says:

- what the matrix covered
- what it did not cover
- what Deezoh did well
- where Deezoh still asked the wrong or weak question
- what to add next:
  - more market conditions
  - more lifecycle outcomes
  - better learning capture
