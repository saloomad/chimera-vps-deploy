# Problem To Feature Map

## "I need the system to keep progress across restarts"

Choose:

- `Task Flow`

Usually pair with:

- `Lobster` for a deterministic subflow
- `Cron` if exact schedule is needed

## "I need a structured multi-step pipeline with clear checkpoints"

Choose:

- `Lobster`

Usually pair with:

- `Task Flow` when the pipeline is part of a durable longer-running flow

## "I need something to fire automatically when a known event happens"

Choose:

- `Hook`

## "I need something to run at 9:00 every day"

Choose:

- `Cron`

## "I need unfinished approved work to wake up later and continue"

Choose:

- `Heartbeat`

## "I need a thesis or memo with several research dimensions"

Choose:

- `deep-research-swarm`

Do not replace the trading loop with this.

## "I need the routine trading cycle to stay lean"

Choose:

- `Task Flow` for durable cycle state
- `Lobster` for bounded deterministic investigation or review subflows
- `Hooks` for event-driven confirmations
- `Cron` only as the wake-up trigger when exact schedule matters
