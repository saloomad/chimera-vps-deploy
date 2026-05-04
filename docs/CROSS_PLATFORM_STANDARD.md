# Cross-Platform Chimera Standard

Updated: 2026-04-28

## Goal

Keep the same Chimera project logic across platforms while still fitting each platform's runtime.

## Same Across All Platforms

- one shared routing contract
- one shared objective orchestration loop
- one shared deep research swarm pattern for evidence-heavy work
- one shared model registry baseline
- one shared GitHub sync contract
- one shared task and action-trace structure
- one shared continuity structure
- one shared task-transition publish contract
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
- shared task-transition state: `session-states/`
- shared unpublished work queue: `publish-queue/`
- platform bootstrap snapshots: `platforms/`
- automation templates: `automation_specs/`
- coordination guard script: `scripts/github_coordination_guard.py`
- coordination verification script: `scripts/verify_github_coordination_system.py`

### Platform Live Repos

- Windows live repo: `saloomad/chimera-windows-live`
- Linux live repo: `saloomad/chimera-linux-live`

## Task-Transition Publish Contract

Do not wait for session end to publish shared truth.

When a platform moves from one meaningful task or bounded slice to another, it must first publish one of these states into the shared repo:

- `published-ready`
- `in-progress-not-ready`
- `blocked-needs-follow-up`

Minimum shared update before another task starts:

1. fetch the coordination repo
2. read `handoffs/`, `session-states/`, and `publish-queue/`
3. update `session-states/<platform>.yaml`
4. update `publish-queue/<platform>.yaml` if code is not ready to publish

This contract exists because continuous sessions still change tasks, and task boundaries are the real continuity risk.

## Required Shared Coordination Skills

All platforms should read:

- `skills/github-coordination-gate`
- `skills/task-transition-publish`
- `skills/platform-live-repo-router`

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
- `deep-research-swarm`
- `openclaw-orchestration-proof-router`
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

Cadence should be chosen from expected pass length and work shape:

- no heartbeat for a `direct task` expected to finish in one pass
- about `5` minutes for very short bounded passes
- about `10` minutes for normal bounded implementation or follow-through passes
- about `15` minutes for medium passes or native VPS work
- `30` minutes or longer only for genuinely long-running or externally gated passes
- update the cadence when the real pass length changes

## Orchestration Classes

Every non-trivial objective should classify itself as one of:

- `direct task`
- `bounded build`
- `deep research swarm`
- `always-on pipeline`

Rules:

- keep `objective-orchestration-loop` as the universal base
- use `deep-research-swarm` only for heavy research, theses, postmortems, and large comparisons
- keep the live trading loop lean and always-on
- do not force the full research swarm into every live cycle

## Live Trading Loop Standard

The normal live trading loop should be:

1. monitor inputs
2. detect setup
3. gather only the needed specialists
4. validate freshness, conflicts, and risk
5. decide `execute`, `watch`, or `reject`
6. manage the position or state
7. review and update state

Use the deep swarm only for bigger jobs such as:

- weekly BTC or market thesis
- major event-driven review
- deep ambiguity that needs cross-verification
- post-trade failure analysis

## Kimi Heartbeat Contract

The Kimi VPS native scheduler path is:

- control file: `/root/openclawtrading/harnesses/codex/chimera/OBJECTIVE_HEARTBEAT.md`
- runner: `/usr/local/bin/run_objective_orchestration_heartbeat.sh`
- service: `kimi-objective-heartbeat.service`
- timer: `kimi-objective-heartbeat.timer`

The timer should only continue work when the control file says `status: active`.
