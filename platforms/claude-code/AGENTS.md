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

Rules:

- plan defines the `ultimate objective`, the current bounded slice, and the done contract
- review may say `complete`, `iterate`, or `blocked`
- use `complete` only when the real user objective is done
- if one slice lands but the broader mission is still open, the correct outcome is `iterate`

Default starter stack for meaningful software work:

1. `prompt-upgrade-engineer`
2. `sal-communication-contract`
3. `vibe-coding-operator`
4. `objective-orchestration-loop`

If the session shows repeated friction or missed activation, also use:

5. `vibe-coding-monitor`

If architecture or system-wide tradeoffs exist, also use:

6. `major-build-council-orchestrator`

If the user wants automatic event enforcement or a stronger pipeline owner, also use:

7. `hook-opportunity-detector`
8. `pipeline-enforcement-detector`
9. `github-coordination-gate`
10. `task-transition-publish`
11. `platform-live-repo-router`
12. `task-change-readiness-gate`

For meaningful replies, always check `sal-communication-contract` before sending the answer so the reply starts with brief context, teaches terms, explains proof artifacts, and ends with a short bottom line plus next step.

Treat `sal-communication-contract` as the single communication source of truth.
Treat `response-structure-enforcer` as compatibility-only.

Do not say only `I changed this` or `I updated that`.
Also explain the important highlight, why that choice was made, what shaped the decision, and what drawback mattered if one existed.

For any meaningful create, build, fix, refactor, workflow change, skill change, or automation change, also run:

- `meaningful-change-lifecycle-and-enforcement-loop.md`
- `docs/PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-02.md`

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
- activation receipts in `trace/platform_activation_receipts.jsonl` for proof of what fired
- shared coordination guards for startup and task-transition proof
