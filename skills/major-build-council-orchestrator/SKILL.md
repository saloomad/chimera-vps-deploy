---
name: major-build-council-orchestrator
description: Run a build council before major or high-tradeoff implementation work, write the chosen path into the objective plan, and hand the result back to objective orchestration for delivery and completion judgment.
triggers:
  - do a council
  - plan first
  - compare options
  - major build
  - architecture change
  - system wide change
  - what path should we choose
---

# Major Build Council Orchestrator

Use this skill when:

- the user explicitly asks for a council
- a build has real architecture or system-wide tradeoffs
- more than one path is credible
- rollback, monitoring, or cross-platform consequences matter enough that one quick opinion is risky

## Core Rule

Council should reduce delivery risk.

Council is not the delivery loop.

The council chooses `chosen_path`.
`objective-orchestration-loop` still owns execution and proof-based completion judgment.

## Required Inputs

- objective
- current reality
- strongest alternatives
- approval boundary
- risks
- whether a file-backed `plan.md` already exists

## Council Roles

Use at least these perspectives:

1. builder / proposer
2. skeptic / critic
3. operator / maintainer
4. tester / verifier
5. final judge

## Output Contract

The council must produce one decision block:

- `problem`
- `alternatives`
- `chosen_path`
- `why_it_won`
- `first_safe_slice`
- `deferrals`
- `invalidation_conditions`
- `proof_shape`

Write that decision into the active `plan.md` when the work is multi-pass.

## Handoff Rule

- council writes `chosen_path`
- orchestration owns execution
- reviewer owns `complete | iterate | blocked`

## Workflow

Also use:

- `C:\Users\becke\claudecowork\workflows\codex\major-build-council-and-delivery-loop.md`
- `C:\Users\becke\claudecowork\workflows\codex\OBJECTIVE_PLAN_TEMPLATE.md`
