# Chimera Codex Bootstrap

Updated: 2026-04-28T19:21:37+03:00
Purpose: one plain-English startup note for Windows Codex so VPS, GitHub, skills, and handoff truth are not split across chat memory.

## Read Order
1. Read this file first.
2. Read `C:\Users\becke\.codex\VPS_CONNECTION.md` for connection and path details.
3. Read `codex-runtime-router` for platform, model, sync, and response-header rules.
4. Read the newest handoff in `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\CHECKPOINT_*.md`.
5. Read `model-registry` before answering model questions.
6. Read `github-manager` before doing GitHub pull, push, sync, or merge work.

## What Changed
- The old Linux PC is no longer the live Chimera machine.
- The live machine is now the Kimi VPS at `root@100.67.172.114`.
- The live Chimera workspace is now `/root/openclawtrading/`.
- GitHub repo `saloomad/chimera-vps-deploy` is the shared cross-platform sync point for handoffs, deploy assets, and shared skill copies.

## Never Use These Old Defaults
- Do not use `open-claw@192.168.1.203`.
- Do not use `open-claw@100.116.214.127`.
- Do not default to `/home/open-claw/...` paths for current VPS work.

## Current Truth Surfaces
- Windows Codex home: `C:\Users\becke\.codex\`
- Windows Chimera workspace: `C:\Users\becke\claudecowork\`
- Shared deploy repo on Windows: `C:\Users\becke\claudecowork\chimera-vps-deploy\`
- Live VPS repo: `/root/chimera-deploy/`
- Live VPS Chimera workspace: `/root/openclawtrading/`
- VPS OpenClaw config: `/root/.openclaw/openclaw.json`

## Skills Codex Should Use
- `model-registry`
  - Use for model names, providers, endpoints, and fallback order.
- `github-manager`
  - Use for cross-platform GitHub sync, pull/push flow, and merge cleanup.
- `codex-runtime-router`
  - Use for platform routing, model lane choice, response header, and session closeout sync.
- `agent-session-resume`
  - Use when continuing from a checkpoint or handoff.

These local skill copies already exist in:
- `C:\Users\becke\.codex\skills\model-registry\SKILL.md`
- `C:\Users\becke\.codex\skills\github-manager\SKILL.md`
- `C:\Users\becke\.codex\skills\codex-runtime-router\SKILL.md`
- `C:\Users\becke\.codex\skills\agent-session-resume\`

## Connection Truth
- SSH target: `ssh root@100.67.172.114`
- VPS home: `/root/`
- VPS Chimera repo: `/root/openclawtrading/`
- If a task mentions the old OpenClaw Linux PC, translate it to the Kimi VPS unless the user explicitly says the old host still matters.

## GitHub Truth
- Shared repo: `saloomad/chimera-vps-deploy`
- Use it for:
  - handoffs
  - shared deploy scripts
  - shared skills that must exist on more than one platform
  - durable cross-platform notes

## Default Sync Pattern
1. Pull the latest `chimera-vps-deploy`.
2. Read the newest `CHECKPOINT_*.md`.
3. If the task needs model answers, read `model-registry`.
4. If the task needs GitHub operations, read `github-manager`.
5. If routing or model choice is unclear, read `codex-runtime-router`.
6. If new durable context was created, update the next checkpoint before ending.

## Response Header

Start replies with:

`Runtime: model=<name> | reasoning=<effort> | quota=<value-or-not-exposed> | phase=<plan|execute|review|mixed> | why=<short reason>`

If live quota is not exposed, say `quota=not exposed`.
Try Codex CLI before claiming quota, but if `codex login status` is all that is available, keep the honest value `not exposed`.

## Platform Routing

- Windows Codex:
  - local implementation, durable continuity, skill work, startup/routing docs
- Windows Claude:
  - planning, architecture, synthesis, cross-platform coordination
- Kimi VPS:
  - live Chimera runtime, Linux services, live repo truth, deploy validation
- GitHub:
  - shared skills, handoffs, deploy scripts, cross-platform pullable truth

## Model Routing

- Planning:
  - prefer `gpt-5.5` with `high` or `xhigh` when the runtime lets you choose
- Execution:
  - prefer `gpt-5.4` with `medium`
- Review:
  - prefer `gpt-5.5` with `high` for judgment-heavy review
  - prefer `gpt-5.4` with `medium` for bounded code review
- Fast mechanical tasks:
  - prefer `gpt-5.4-mini` with `low`

Current local default from `config.toml`:
- model = `gpt-5.4`
- reasoning = `medium`

Important:
- automatic hidden per-task model switching is not yet verified in this runtime
- treat this as a routing rule and visible declaration, not a fake claim that the app auto-switched behind the scenes
- spawned agents inherit the parent model by default unless there is a clear reason to override
- if the result quality is weak, rerun on a stronger reasoning level or stronger model and record that lesson in closeout

## Session Closeout Sync

Every meaningful session should capture:

- skills created
- skills updated
- other durable files created
- routing used:
  - planning / execution / review / research
  - model
  - reasoning
  - result quality
- sync status:
  - local only
  - shared in repo but not pushed yet
  - pushed and available to other platforms

If a shared skill changed, mirror it into `chimera-vps-deploy/skills/` and mention it in the newest checkpoint.

## Platforms In This Loop
- Windows Claude: planning, setup, docs, coordination
- Windows Codex: implementation, local workspace work, durable continuity
- VPS OpenClaw: live Chimera runtime
- space-agent.ai: web agent that should consume the same GitHub handoff truth

## Practical Rule
If Codex has to choose between chat memory and one of these files, trust these files first:
- `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
- `C:\Users\becke\.codex\VPS_CONNECTION.md`
- `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\CHECKPOINT_*.md`
- `C:\Users\becke\.codex\skills\codex-runtime-router\SKILL.md`
- `C:\Users\becke\.codex\skills\model-registry\SKILL.md`
- `C:\Users\becke\.codex\skills\github-manager\SKILL.md`
