# Failure Taxonomy

Use these labels so reviews are comparable.

## Truth Surface Mismatch

- the wrong file or runtime surface was treated as truth

## Producer Consumer Mismatch

- producer wrote something but the consumer did not use it

## Route Selection Error

- the wrong proof lane or wrong owner was chosen

## State Transition Drift

- workflow advanced, regressed, or branched incorrectly

## Instruction Behavior Gap

- the instructions say one thing, but the behavior says another

## Tool Or Runtime Defect

- the tool, wrapper, environment, or script failed mechanically

## Scenario Coverage Gap

- the existing tests do not cover the failure we care about

## Scoring Bias

- the grading method is circular, too soft, or derived from the same artifact under test

## Observability Gap

- the system cannot show why the decision happened

## Live Unproven

- local or replay proof exists, but real runtime proof still does not
