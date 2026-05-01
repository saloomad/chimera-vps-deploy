# Vibe Coding Operator Monitor And Improvement Loop

## Trigger

Use this workflow when:

- the `vibe-coding-operator` skill changes
- Sal says agents should work with him better
- orchestration did not auto-trigger clearly enough
- the same friction keeps happening across sessions
- we need to test discoverability, routing, or enforcement quality

## Required Inputs

- current `vibe-coding-operator` skill
- current `objective-orchestration-loop` skill
- current `vibe-coding-monitor` skill
- current `prompt-upgrade-engineer` skill
- relevant `AGENTS.md` or platform instruction files
- latest handoff and any orchestration issue notes

## Loop

1. Restate the improvement objective in plain English.
2. Define the objective contract:
   - objective
   - orchestration class
   - current reality
   - done criteria
   - last proof
   - next step
   - stop condition
3. Check the starter stack:
   - did `prompt-upgrade-engineer` run
   - did `vibe-coding-operator` activate
   - did `objective-orchestration-loop` activate
   - should `vibe-coding-monitor` run before closeout
4. Run a scenario check against the main use cases:
   - tiny one-line ask
   - meaningful build request
   - "keep going until done" request
   - beginner explanation request
   - project-management cleanup request
   - postmortem / interaction-friction request
   - cross-platform continuation request
5. For each scenario, record:
   - expected skill activation
   - expected orchestration class
   - expected proof and closeout behavior
   - whether the current rule set would likely pass
6. If a scenario fails, classify the gap:
   - prompt issue
   - skill activation gap
   - orchestration gap
   - recommendation quality issue
   - interaction learning gap
   - platform drift
7. Apply the smallest useful improvement:
   - skill rule
   - workflow rule
   - AGENTS/platform instruction rule
   - research/wiki capture
   - issue ledger update
8. Re-check the scenario that failed.
9. Close out with:
   - what improved
   - what still depends on instruction-following rather than hard enforcement
   - next platform or scenario to test

## Expected Outputs

- updated skill or workflow files when safe
- updated platform instructions when discoverability was weak
- updated research/wiki capture when a reusable lesson was learned
- an orchestration issue entry when activation or loop behavior failed
- a short scorecard of what now passes and what still does not

## Stop Or Escalate

Stop when:

- the target scenario passes honestly
- the current improvement slice is complete
- a safe next step is recorded

Escalate when:

- the platform lacks a real enforcement surface
- the fix would need product/runtime support that we do not control
- the right behavior is still ambiguous after reading the local rules
