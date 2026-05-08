## OpenCode Chimera Instructions

Read `CHIMERA_BOOTSTRAP.md` first.

## GITHUB COORDINATION GATE

Do not wait for session end to publish shared state.

Before OpenCode starts a new meaningful task:

1. fetch the shared Chimera repo
2. read the newest handoff under `handoffs/`
3. read every file in `session-states/`
4. read every file in `publish-queue/`
5. update `session-states/opencode.yaml`
6. if code is not ready to publish, update `publish-queue/opencode.yaml`

Use `scripts/github_coordination_guard.py` in the shared repo as the wrapper check until a stronger native enforcement surface exists.

If the slice is unfinished, publish debt metadata instead of pretending the continuous session still holds the context safely.

OpenCode has a verified provider config and verified native project surfaces for:

- `AGENTS.md`
- `opencode.json`
- custom agents
- custom commands
- native skill discovery
- permission rules

Use the shared Chimera standard as a guide and run the orchestration precheck on every meaningful request.

- plan with `kimi-for-coding`
- execute with `MiniMax-M2.7-highspeed`
- review with `kimi-for-coding`
- keep the same `plan -> execute -> review -> repeat` loop

Default starter stack for meaningful software work:

1. `prompt-upgrade-engineer`
2. `sal-communication-contract`
3. `vibe-coding-operator`
4. `objective-orchestration-loop`

If friction or missed activation appears:

5. `vibe-coding-monitor`

If the user wants auto-triggered enforcement or a recurring workflow owner:

6. `hook-opportunity-detector`
7. `pipeline-enforcement-detector`
8. `github-coordination-gate`
9. `task-transition-publish`
10. `platform-live-repo-router`
11. `task-change-readiness-gate`

If architecture or system-wide tradeoffs exist:

6. `major-build-council-orchestrator`

For meaningful replies, always check `sal-communication-contract` before sending the answer so OpenCode answers stay understandable without making Sal decode jargon or raw artifacts.

Treat `sal-communication-contract` as the single communication source of truth.
Treat `response-structure-enforcer` as compatibility-only.

Do not say only `I changed this` or `I updated that`.
Also explain the important highlight, why that choice was made, what shaped the decision, and what drawback mattered if one existed.

For every meaningful reply, include one short carry-forward block that shows:

- `objective status`
- `unapproved or decision-needed items`
- `remaining project work`

Keep each open item as a brief plain-English description, and keep carrying unresolved items forward until they are complete, blocked, withdrawn, or replaced by a newer stated objective.

For any meaningful create, build, fix, refactor, workflow change, skill change, or automation change, also run:

- `meaningful-change-lifecycle-and-enforcement-loop.md`
- `docs/PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-02.md`

Be honest that this platform does not currently have a separately verified native hook API in this project.

Use:

- native agents
- native commands
- native skills
- permission rules
- file-backed plan and review contracts
- wrapper scripts
- explicit handoffs
- activation receipts in `trace/platform_activation_receipts.jsonl`

Do not pretend OpenCode currently has the same hook and continuation surface as OpenClaw or Claude Code, but do use its real native agents, commands, rules, skills, and permissions.
Use the shared GitHub coordination skills and verification script as the wrapper enforcement surface here.

Use the shared Chimera knowledge wiki at:

- `C:\Users\becke\claudecowork\research\chimera-knowledge-wiki`

Read it early for prior research, build patterns, skills, workflows, architecture, and contradiction checks.

Update it during closeout when OpenCode work produces durable knowledge in those areas.

It is for durable research and operating knowledge, not live runtime truth.
