# Orchestration Challenge Results

Updated: 2026-04-30

## Purpose

This note records a bounded proof run against the upgraded orchestration rules.

## Test Design

The proof used:

- three cheap first-pass workers
- one stronger review worker

The cheap workers were asked to classify and route:

1. a weekly Bitcoin thesis
2. a routine live BTC setup watcher
3. a failure case with weak and contradictory dimension files

The stronger reviewer then judged whether the cheap-worker answers were good enough.

## Scenario 1 - Weekly Bitcoin Thesis

### Result

The worker correctly chose:

- `deep research swarm`

It also correctly named:

- multi-timeframe technicals
- ETF flows
- on-chain activity
- derivatives
- macro
- alt rotation

### What Passed

- correct orchestration class
- correct role family
- correct file-first direction

### What Was Still Thin

- freshness rule was not explicit enough
- done criteria and stop condition were not explicit enough

## Scenario 2 - Routine Live BTC Watcher

### Result

The worker correctly refused swarm mode and chose:

- `always-on pipeline`

### What Passed

- anti-swarm discipline held
- the lean loop stayed focused on routine monitoring and decisioning

### What Was Still Thin

- the answer compressed the lean loop too much
- it needed clearer mention of specialist gathering, position-state management, and review/update state

## Scenario 3 - Weak And Contradictory Dimension Files

### Result

The worker correctly:

- failed the gate after cross-verification
- chose targeted validation
- reran only the failed slices
- refused to restart the whole swarm

### What Passed

- narrow rerun logic
- anti-fake-certainty behavior

### What Was Still Thin

- it needed clearer wording that unresolved uncertainty must stay visible if validation cannot fully resolve the conflict

## Strong Review Verdict

The stronger reviewer judged the upgrade as:

- `pass with caveats`

Main conclusion:

- the orchestration rules are mostly right
- cheap-worker routing is directionally good
- but the cheap-worker response format needed a stricter schema so workers return the full contract, not only the class label

## Fix Applied After Review

The skill was tightened further by adding a required cheap-worker verdict schema with fields for:

- orchestration class
- why not the other classes
- freshness requirement
- required artifacts
- required gates
- stop condition
- rerun policy
- escalation policy

## Final Read

The system is now stronger than before this proof run because:

- it captures the research more concretely
- it documents the role set and file contract
- it now has a tighter cheap-worker judgment shape
