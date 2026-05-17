# Review Debug Output Contract

Every non-trivial run should leave one compact result object or written equivalent with:

- `target`
- `route`
- `failure_taxonomy`
- `minimal_failing_repro`
- `expected_vs_observed`
- `hypothesis`
- `counter_hypothesis`
- `evidence_used`
- `deterministic_check`
- `scorecard`
- `winner_or_verdict`
- `regressions`
- `still_unproven`

## Interpretation Rules

- `hypothesis` is the leading explanation.
- `counter_hypothesis` is the strongest alternative explanation that still needed to be ruled out.
- `deterministic_check` must say what repeatable check was run or why no honest repeatable check existed yet.
- `scorecard` can be narrative or structured, but it must distinguish:
  - reasoning-quality findings
  - deterministic-proof findings
  - live-vs-replay confidence

## Minimum Standard

If a run cannot name a `minimal_failing_repro` or `expected_vs_observed`, it is still exploration, not yet a finished debug review.
