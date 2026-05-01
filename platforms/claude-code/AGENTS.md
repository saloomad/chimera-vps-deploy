## Claude Code Chimera Instructions

Read `CHIMERA_BOOTSTRAP.md` first.

Use the shared `objective-orchestration-loop` skill as an every-message orchestration precheck.

For each meaningful request, say:

- whether the full loop is needed
- which orchestration class fits
- why that route fits
- what the done contract is

Mandatory process:

`plan -> execute -> review -> repeat`

Default starter stack for meaningful software work:

1. `prompt-upgrade-engineer`
2. `vibe-coding-operator`
3. `objective-orchestration-loop`

If the session shows repeated friction or missed activation, also use:

4. `vibe-coding-monitor`

If architecture or system-wide tradeoffs exist, also use:

5. `major-build-council-orchestrator`

Use the same logic as the other Chimera platforms, but keep Claude Code's limits honest:

- no durable native heartbeat after close
- continuity depends on files
- if a task must survive close or run on a timer, route it to a platform with persistent automation support

Preferred phase routing:

- plan: strongest available model
- execute: current coding model
- review: stronger model if the output is weak or ambiguous

Claude Code-specific enforcement surfaces to prefer:

- hooks
- slash commands
- subagents
- `CLAUDE.md`

Best hook uses here:

- `UserPromptSubmit` for orchestration precheck
- `PreToolUse` and `PostToolUse` for guardrails and proof capture
- slash commands for repeatable orchestration entry points
