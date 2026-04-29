# Cross-Platform Chimera Standard

Updated: 2026-04-28

## Goal

Keep the same Chimera project logic across platforms while still fitting each platform's runtime.

## Same Across All Platforms

- one shared routing contract
- one shared objective orchestration loop
- one shared model registry baseline
- one shared GitHub sync contract
- one shared task and action-trace structure
- one shared continuity structure
- one shared simulation and backtest standard
- one shared rule that objectives continue until done or blocked

## Platform-Optimized Differences

### Windows Codex

- local skill home: `C:\Users\becke\.codex\skills\`
- local bootstrap: `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
- local automations live under `C:\Users\becke\.codex\automations\`

### Kimi VPS

- local skill home: `/root/.kimi/skills/`
- local bootstrap: `/root/.kimi/CHIMERA_BOOTSTRAP.md`
- live runtime repo: `/root/openclawtrading/`
- shared deploy repo: `/root/chimera-deploy/`
- native heartbeat runner: `kimi-objective-heartbeat.timer`

### Shared GitHub Repo

- shared skill source: `skills/`
- shared handoffs: `handoffs/`
- platform bootstrap snapshots: `platforms/`
- automation templates: `automation_specs/`

## Required Project Structure Families

Mirror these across the platforms that own Chimera work:

- `harnesses/codex/chimera/`
- `tasks/`
- `trace/`
- `skills/`
- platform bootstrap and instruction files

## Required Shared Skills

- `codex-runtime-router`
- `model-registry`
- `github-manager`
- `project-operations-manager`
- `agent-session-resume`
- `openclaw-replay-and-backtest`
- `strategy-backtest-lab`
- `pipeline-simulation-lab`
- `openclaw-workspace`

## Heartbeat Standard

Heartbeat or recurring continuation flows should:

1. restate the objective and done criteria
2. run a short `plan` phase
3. run the next bounded `execute` phase
4. run a `review` phase that decides `complete`, `iterate`, or `blocked`
5. stop only on completion, blocker, or approval boundary
6. update continuity and task/action truth after meaningful progress
7. leave a clean next action for the next wake or next session

## Kimi Heartbeat Contract

The Kimi VPS native scheduler path is:

- control file: `/root/openclawtrading/harnesses/codex/chimera/OBJECTIVE_HEARTBEAT.md`
- runner: `/usr/local/bin/run_objective_orchestration_heartbeat.sh`
- service: `kimi-objective-heartbeat.service`
- timer: `kimi-objective-heartbeat.timer`

The timer should only continue work when the control file says `status: active`.
