# Worker Verdict Schema

Use this when a cheaper worker is making a first-pass orchestration call.

The goal is to return an enforceable contract, not just a loose recommendation.

## Required Fields

```json
{
  "scenario": "",
  "orchestration_class": "",
  "why_not_other_classes": [],
  "freshness_requirement": "",
  "required_artifacts": [],
  "required_gates": [],
  "stop_condition": "",
  "rerun_policy": "",
  "escalation_policy": ""
}
```

## Field Meaning

### `orchestration_class`

One of:

- `direct task`
- `bounded build`
- `deep research swarm`
- `always-on pipeline`

### `why_not_other_classes`

Say why the rejected classes are wrong.
This helps catch overuse of the swarm.

### `freshness_requirement`

State the time horizon or date rule.

Examples:

- `same-day sources required for market-moving claims`
- `point-in-time historical context only`
- `freshness not critical; durable codebase truth is enough`

### `required_artifacts`

List the minimum state or output files.

Examples:

- `plan.md`
- `research/landscape_brief.md`
- `research/dim01.md`
- `research/cross_verification.md`
- `final/report.md`

### `required_gates`

List the gates that must pass before advancing.

Examples:

- `dimensions distinct but overlapping`
- `all required dimension files exist`
- `conflicts explicitly classified`
- `writing does not hide the conflict zone`

### `stop_condition`

State when this path should stop.

Examples:

- `stop on complete`
- `stop on blocked`
- `stop after 3 no-progress wakes and require human input`

### `rerun_policy`

State what gets rerun if quality fails.

Examples:

- `rerun only failed or ambiguous slices`
- `do not restart the whole swarm by default`

### `escalation_policy`

State when the model or reasoning lane should escalate.

Examples:

- `raise reasoning first`
- `rerun review on a stronger lane if conflict remains`
- `escalate only failed slices, not the whole job`
