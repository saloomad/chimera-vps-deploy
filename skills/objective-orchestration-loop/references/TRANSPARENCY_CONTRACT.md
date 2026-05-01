# Orchestration Transparency Contract

Use this compact contract whenever the task is meaningful enough that the user should see the orchestration logic.

## Minimum Visible Fields

- `orchestration_decision`
- `orchestration_class`
- `reason_for_route`
- `objective`
- `done_contract`
- `current_phase`
- `next_step`
- `review_outcome`

## Recommended Compact Shape

`orchestration_decision: light orchestration`

`orchestration_class: bounded build`

`reason_for_route: several real changes and proof steps are needed, so a direct answer would hide too much`

`objective: make the shared orchestration skill visible and platform-aware`

`done_contract: shared skill updated, platform adapters updated, research captured, live proof done where supported`

`current_phase: execute`

`next_step: patch the shared skill and platform adapters`

`review_outcome: iterate`

## When To Add Dimensions

Add `dimensions` only when the work has real separable lanes, such as:

- several platforms
- several independent evidence lanes
- several design surfaces like hooks, flows, and schedulers

Do not add dimensions to small work just to look thorough.
