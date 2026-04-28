## Claude Code Chimera Instructions

Read `CHIMERA_BOOTSTRAP.md` first.

Use the shared `objective-orchestration-loop` skill for every non-trivial task.

Mandatory process:

`plan -> execute -> review -> repeat`

Use the same logic as the other Chimera platforms, but keep Claude Code's limits honest:

- no durable native heartbeat after close
- continuity depends on files
- if a task must survive close or run on a timer, route it to a platform with persistent automation support

Preferred phase routing:

- plan: strongest available model
- execute: current coding model
- review: stronger model if the output is weak or ambiguous
