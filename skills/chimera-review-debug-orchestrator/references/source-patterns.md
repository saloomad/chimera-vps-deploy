# Source Patterns

## Local Skills To Reuse

- `pipeline-simulation-lab`
  - best for desk and workflow behavior
- `strategy-backtest-lab`
  - best for strategy edge and walk-forward testing
- `openclaw-replay-and-backtest`
  - best for historical artifact replay
- `chimera-bundle-consumer-simulation`
  - best for Deezoh packet usefulness and phase-transition judgment
- `learning-loop`
  - best for turning failures into durable reviewed lessons
- `openclaw-taskflow-architect`
  - best for durable restart-safe state ownership
- `openclaw-lobster-workflow-designer`
  - best for deterministic phase workflows

## External Skill Patterns Reviewed

- `anthropics/knowledge-work-plugins@pipeline-review`
  - useful pattern: health scoring and actionable next steps
  - not directly reusable as-is because it is CRM/pipeline oriented, not Chimera phase-state oriented

- `charon-fan/agent-playbook@workflow-orchestrator`
  - useful pattern: milestone-based follow-up routing
  - not enough by itself for replay/backtest or market artifact truth

- `wshobson/agents@backtesting-frameworks`
  - useful pattern: event-driven backtesting architecture with positions, fills, and execution modeling
  - useful as a conceptual source for more realistic lifecycle replay and execution simulation

## Design Conclusion

The right universal skill here is not a replacement skill.

It should be a routing and proof skill that:

- chooses the correct lane
- runs the proof
- merges failures
- creates the improvement queue
