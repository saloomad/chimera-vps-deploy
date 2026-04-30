# Skill Combination Matrix

The deep swarm is one layer, not the whole operating model.

## Minimum Companion Set

| Skill | Why it should usually be paired |
|---|---|
| `objective-orchestration-loop` | chooses whether the task is really a deep swarm at all |
| `codex-runtime-router` | assigns phase, platform, model, and reasoning level |
| `model-registry` | gives current model facts, pricing, and benchmark context |

## OpenClaw And Trading Pairings

| Skill | When to combine |
|---|---|
| `openclaw-orchestration-proof-router` | when OpenClaw, Lobster, Task Flow, hooks, or heartbeat choices matter |
| `pipeline-simulation-lab` | when testing desk behavior or orchestration behavior in scenarios |
| `strategy-backtest-lab` | when testing strategy edge rather than orchestration behavior |
| `openclaw-replay-and-backtest` | when replaying real or synthetic market conditions |

## Project And Continuity Pairings

| Skill | When to combine |
|---|---|
| `project-operations-manager` | when the work should update project or task truth |
| `agent-session-resume` | when resuming prior state from durable files |
| `codex-task-and-project-capture` | when the swarm creates new follow-ups or blockers |
| `codex-continuity-enforcer` | after meaningful durable work |
| `codex-lesson-harvester` | when the swarm teaches a reusable lesson |

## Anti-Pattern Rules

Do not combine the deep swarm with:

- every routine monitor cycle
- every simple coding task
- every live trading wake
- every alert triage pass

If the work is routine, keep it in `objective-orchestration-loop` as a `direct task`, `bounded build`, or `always-on pipeline`.
