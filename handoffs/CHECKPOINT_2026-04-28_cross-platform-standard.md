# Agent Session Handoff - Chimera Ecosystem

## Session Info
- **Ended by**: Windows Codex
- **Ended at**: 2026-04-28T22:30:00+03:00
- **Platform**: Windows Codex
- **Session focus**: cross-platform routing, shared skill promotion, Kimi VPS bootstrap, and standard project-structure sync

## Original Goal
Make the important Chimera instructions, routing, skills, continuity structure, and simulation/backtest stack behave the same across platforms while still fitting each platform's native home and runtime.

## Completed Work
- [x] Expanded shared `codex-runtime-router` and `model-registry` so model selection, reasoning level, reruns, route self-grade, and benchmark/cost guidance are durable.
- [x] Promoted the missing shared skills into `chimera-vps-deploy/skills/`: `agent-session-resume`, `project-operations-manager`, `openclaw-replay-and-backtest`, `strategy-backtest-lab`, `pipeline-simulation-lab`, and `openclaw-workspace`.
- [x] Added platform standard files to the shared repo: `platforms/windows-codex/`, `platforms/kimi-vps/`, `docs/CROSS_PLATFORM_STANDARD.md`, and shared automation templates under `automation_specs/`.
- [x] Installed the shared core set onto the live Kimi VPS in `/root/.kimi/skills/` and updated `/root/.kimi/{AGENTS.md,CHIMERA_BOOTSTRAP.md}`.
- [x] Synced Chimera continuity/task/trace structure onto the live VPS repo under `/root/openclawtrading/{harnesses/codex/chimera,tasks,trace}`.

## Partially Done
- [~] The live VPS now has the shared core set, but no proof run has been done yet showing a fresh Kimi session actually following the new bootstrap and routing files from start to finish.

## Not Done
- [ ] Create or wire true platform-native recurring automations on non-Codex platforms from the shared `automation_specs/` templates.

## Decisions Made
- **Decision**: GitHub should carry the shared core skills, platform bootstrap snapshots, automation templates, and project-structure standard. | **Why**: it gives every platform one pullable source of truth while still allowing native path differences.
- **Decision**: keep platform optimization local to each platform's bootstrap and AGENTS files, not by forking the core skill logic. | **Why**: same logic, fewer drift points.

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| `skills/codex-runtime-router/` | Shared | Added fuller routing, reasoning, rerun, self-grade, and reference-sheet logic |
| `skills/model-registry/SKILL.md` | Shared | Rebuilt around current OpenAI, MiniMax, and Kimi routing facts |
| `skills/{agent-session-resume,project-operations-manager,openclaw-replay-and-backtest,strategy-backtest-lab,pipeline-simulation-lab,openclaw-workspace}/` | Shared | Promoted into shared repo for pull-based sync |
| `platforms/windows-codex/{AGENTS.md,CHIMERA_BOOTSTRAP.md}` | Shared snapshot | Captured current Windows Codex startup standard |
| `platforms/kimi-vps/{AGENTS.md,CHIMERA_BOOTSTRAP.md}` | Shared | Added Kimi-native startup and routing standard |
| `docs/CROSS_PLATFORM_STANDARD.md` | Shared | Added same-structure and same-logic contract |
| `automation_specs/*/automation.toml` | Shared | Added shared heartbeat and recurring-run templates |

## Skills Created / Updated
- [x] `codex-runtime-router` - updated - shared in repo
- [x] `model-registry` - updated - shared in repo
- [x] `github-manager` - updated - shared in repo
- [x] `agent-session-resume` - shared skill copy added - shared in repo
- [x] `project-operations-manager` - shared skill copy added - shared in repo
- [x] `openclaw-replay-and-backtest` - shared skill copy added - shared in repo
- [x] `strategy-backtest-lab` - shared skill copy added - shared in repo
- [x] `pipeline-simulation-lab` - shared skill copy added - shared in repo
- [x] `openclaw-workspace` - shared skill copy added - shared in repo

## Other Durable Outputs Created
- [x] `docs/CROSS_PLATFORM_STANDARD.md` - shared in repo
- [x] `platforms/kimi-vps/*` - shared in repo
- [x] `platforms/windows-codex/*` - shared in repo
- [x] `automation_specs/*/automation.toml` - shared in repo

## Sync Status
- **GitHub status**: local shared repo updated but not pushed yet
- **Other platforms that should pull this**: Windows Codex, Kimi VPS, space-agent.ai, any future OpenClaw Codex surface
- **What still needs sync**: push `chimera-vps-deploy` to GitHub; after that, any non-live platform should pull the repo and install shared skills from `skills/`

## Routing Used
- **Task lane**: mixed
- **Model used**: gpt-5.4
- **Reasoning used**: medium
- **Result quality**: strong
- **Rerun needed**: no
- **Better route next time**: same, unless the job becomes architecture-heavy enough to justify a planning-only `gpt-5.5` pass first

## Next Actions (for next agent)
1. **[PRIORITY]** Push `chimera-vps-deploy` so the shared skill and platform-standard changes become pullable everywhere.
2. **[MEDIUM]** Start one fresh Kimi session on the VPS and verify it reads `/root/.kimi/CHIMERA_BOOTSTRAP.md`, the shared routing skill, and the shared model registry.
3. **[LOW]** Turn the shared `automation_specs/` templates into real platform-native scheduled runs where the platform exposes that feature.

## Skills to Read Before Starting
- [x] `codex-runtime-router` - for platform and model routing
- [x] `model-registry` - for model choice, benchmarks, and costs
- [x] `github-manager` - for GitHub sync work
- [x] `agent-session-resume` - when continuing this handoff
- [x] `openclaw-replay-and-backtest` - for replay proof
- [x] `strategy-backtest-lab` - for strategy-only history tests
- [x] `pipeline-simulation-lab` - for Deezoh and workflow simulation

## Live System State (if applicable)
- **Kimi native home**: `/root/.kimi/` now exists with shared bootstrap and AGENTS files
- **Kimi shared skills installed**: yes, core set installed under `/root/.kimi/skills/`
- **OpenClaw runtime repo standard structure**: `harnesses/codex/chimera`, `tasks/TASK_REGISTRY.md`, and `trace/ACTION_LOG.md` now exist under `/root/openclawtrading/`

## Reading List for Next Agent
- `docs/CROSS_PLATFORM_STANDARD.md`
- `platforms/kimi-vps/CHIMERA_BOOTSTRAP.md`
- `skills/codex-runtime-router/references/MODEL_ROUTING_SPEC.md`
