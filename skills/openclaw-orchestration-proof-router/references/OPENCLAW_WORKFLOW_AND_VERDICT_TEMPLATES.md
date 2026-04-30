# OpenClaw Workflow And Verdict Templates

Use these as small OpenClaw-specific adapters around the shared orchestration core.

## 1. OpenClaw Routing Verdict Template

```json
{
  "orchestration_class": "",
  "chosen_openclaw_pattern": "",
  "why_not_other_patterns": [],
  "freshness_requirement": "",
  "required_artifacts": [],
  "required_gates": [],
  "stop_condition": "",
  "rerun_policy": "",
  "escalation_policy": ""
}
```

### `chosen_openclaw_pattern`

One of:

- `lobster`
- `task flow`
- `heartbeat`
- `hooks`
- `timer only`
- `direct path`

## 2. Pattern Choice Rules

### Choose `lobster`

When:

- the flow is deterministic
- several steps or branches depend on each other
- you need visible gates and conditional reruns

### Choose `task flow`

When:

- restartable state matters most
- the workflow must recover after interruption

### Choose `heartbeat`

When:

- the objective needs recurring continuation
- safe approved work should resume across wakes

### Choose `hooks`

When:

- you need event-driven validation or reactions

### Choose `timer only`

When:

- the timer is only there to wake the real workflow

## 3. OpenClaw Human Proof Checklist

- what pattern was chosen
- why the others were rejected
- where the state lives
- which gate is current
- which worker or agent owns the next step
- whether the loop is still active or should stop
