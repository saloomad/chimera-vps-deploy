# Feature Decision Matrix

## Use `Lobster`

When:

- the flow is deterministic
- the steps are known ahead of time
- you want one structured pipeline call instead of many manual tool calls
- approvals or explicit checkpoints matter

Do not use it for:

- long-lived durable state by itself
- open-ended research swarms
- pure event reactions

## Use `Task Flow`

When:

- work spans multiple steps or branches
- restart-safe progress matters
- you need a durable flow state above individual background tasks
- the flow should survive gateway restarts

Do not use it for:

- a single isolated background task
- a simple one-shot reminder
- a pure event trigger

## Use `Hooks`

When:

- an event should trigger the action
- the action belongs to startup, bootstrap, command, message, or lifecycle events
- the feature should run automatically when a known event fires

Do not use it for:

- exact-time scheduling
- large multi-step durable state by itself

## Use `Cron`

When:

- timing must be exact
- the job should run isolated from the current chat
- the job is mostly a wake-up or scheduled batch

## Use `Heartbeat`

When:

- approved work needs continuation across wakes
- you need periodic stall detection or status checks

Do not use it as:

- the main orchestration design
- a replacement for Task Flow

## Use `Deep Research Swarm`

When:

- the objective is evidence-heavy
- several dimensions need cross-verification
- the output is a memo, thesis, postmortem, or large comparison

Do not use it for:

- the routine live trading cycle
- simple coding or monitor tasks
