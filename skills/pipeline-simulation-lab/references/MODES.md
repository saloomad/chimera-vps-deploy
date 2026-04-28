# Pipeline Simulation Modes

## Default Execution Rule

If the mode is being used to answer "what would the desk, Deezoh, or the council do?", run agents first.

Use the deterministic helper only to:
- package cases
- validate inputs
- collate outputs
- score or compare captured runs

Do not let a helper script replace the real agent behavior run.

## `scenario-suite`

Fastest regression mode.

Best for:
- did we break the desk logic
- did contracts still produce the expected state
- quick proof after a prompt or workflow change

Use this as a preflight or regression check, not as the only proof when the goal is behavior simulation.

## `variant-compare`

Best for:
- comparing several desk models
- measuring council value
- measuring timeframe handoff value
- seeing which version handles mixed cases better

For a real behavior comparison, run each variant through isolated agent simulations and use the helper only to compare the captured results.

## `a-b-test`

Best for:
- compare two implementations directly
- compare old instructions vs new instructions
- compare two enforcement designs

Run the same scenario through agent-executed variants first, then score the outputs.

## `failure-injection`

Best for:
- stale core reports
- missing strategy evidence
- unknown gate behavior
- mixed bias
- market-maker block behavior
- trigger-missing behavior

The failure should be injected into the scenario, then observed through agent behavior.

## `live-snapshot-compare`

Best for:
- turning the current report surface into one bounded case
- seeing whether the desk variants disagree
- exposing whether the snapshot is truly live or only a local mirror

Important truth:
- if the source is only a local report folder, this is a local snapshot compare, not verified live runtime truth

## `instruction-a-b`, `enforcement-a-b`, `build-compare`

Best for:
- comparing two result sets from the generic agent scenario lab
- testing whether a new prompt, instruction layer, or build behaves better
- catching regressions like fake completion, re-approval loops, or unsafe fallback behavior

## `orchestration`

Best for:
- one bounded combined pass
- fast regression suite plus variant compare
- failure injection
- snapshot audit
- optional build/instruction compare in one report

Important truth:
- orchestration mode is analysis-only by default
- it will stop after a bounded pass unless you add a real auto-fix hook later
- orchestration should coordinate agent-run simulations first and only use helper logic for aggregation

## Important Truth

These pipeline modes are fast workflow simulations.

They are not yet the same thing as a full historical every-agent replay where each agent only knows what was available at that exact moment.
They are still very useful for:
- routing
- state transitions
- council behavior
- process quality
- decision consistency
