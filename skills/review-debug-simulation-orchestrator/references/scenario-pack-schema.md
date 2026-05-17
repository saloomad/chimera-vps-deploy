# Scenario Pack Schema

Use one reusable scenario shape for review, debug, and simulation work.

## Required Fields

- `id`
- `goal`
- `target`
- `route_hint`
- `fixtures`
- `mutations`
- `expected_good`
- `expected_bad`
- `scoring_dimensions`
- `consumer`
- `limitations`

## Suggested Optional Fields

- `freshness_rules`
- `baseline_version`
- `candidate_version`
- `risk_level`
- `red_team_tags`
- `owner_hypothesis`

## Route Hints

- `reasoning_review`
- `artifact_check`
- `replay`
- `simulation`
- `backtest`
- `red_team`
- `ab_compare`

## Mutation Examples

- delete one required field
- stale one source
- contradict two sources
- change the owner
- force an illegal transition
- make no-trade the correct outcome
- make one helper source misleading but present
