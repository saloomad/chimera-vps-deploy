# Chimera Kimi VPS Bootstrap

Updated: 2026-04-28
Purpose: one startup note for the Kimi VPS so local Kimi sessions, OpenClaw runtime work, and shared GitHub sync all start from the same truth.

## Read Order

1. Read this file first.
2. Read `AGENTS.md` in the same folder.
3. Pull the latest `chimera-vps-deploy`.
4. Read the newest `handoffs/CHECKPOINT_*.md`.
5. Read the shared skills:
   - `skills/objective-orchestration-loop`
   - `skills/codex-runtime-router`
   - `skills/model-registry`
   - `skills/github-manager`
   - `skills/github-coordination-gate`
   - `skills/task-transition-publish`
   - `skills/platform-live-repo-router`
   - `skills/task-change-readiness-gate`
   - `skills/project-operations-manager`
   - `skills/agent-session-resume`
   - `skills/openclaw-replay-and-backtest`
   - `skills/strategy-backtest-lab`
   - `skills/pipeline-simulation-lab`

## Platform Truth

- Native Kimi home: `/root/.kimi/`
- Native Kimi skills home: `/root/.kimi/skills/`
- Live Chimera runtime repo: `/root/openclawtrading/`
- Shared deploy repo: `/root/chimera-deploy/`
- Linux live repo: `saloomad/chimera-linux-live`
- Live OpenClaw config: `/root/.openclaw/openclaw.json`

## Shared Routing Rules

- plan execute review is mandatory for non-trivial objectives
- Planning: prefer the strongest available model with high reasoning
- Execution: prefer the cheaper stable implementation lane
- Review: rerun on a stronger lane when the first result is weak
- Quota honesty: if the platform does not expose quota, say so plainly
- Result self-grade: capture model, reasoning, result quality, rerun need, and better route next time

## Shared Skill Rule

If a shared skill changes:

1. update it in `chimera-deploy/skills/`
2. install or copy it into `/root/.kimi/skills/`
3. mention the sync state in the latest handoff
4. do not call it synced unless the GitHub repo is pushed and the local Kimi copy is updated

## Knowledge Capture Rule

If a Kimi/OpenClaw session creates durable knowledge about:

- research
- build patterns
- skills or workflows
- architecture decisions
- contradictions across sources

then update the Chimera knowledge wiki before closeout or record plainly why capture was deferred.

Default VPS wiki:

- `/root/openclawtrading/research/chimera-knowledge-wiki`

## Same Project Structure Rule

For the same Chimera project, keep these structure families aligned across platforms:

- `harnesses/codex/chimera/`
- `tasks/`
- `trace/`
- shared `skills/`
- platform bootstrap and instruction files

If the live runtime repo is missing one of these folders, sync it or record the gap plainly.
