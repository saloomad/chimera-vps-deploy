# Platform Capability Comparison — Hermes vs OpenClaw vs Codex

**Purpose:** When the user asks to "import OpenClaw into Hermes" or "use OpenClaw's enforcement in Hermes," this reference provides the canonical answer. It explains what each platform can actually do, not just how to connect to them.

**Last updated:** 2026-05-15

---

## The Core Insight

**Enforcement is a runtime, not a library.**

Skills, workflows, and hook definitions are just files. What makes OpenClaw's lobster/hooks work is the *runtime* that executes them:
- Lobster runner (`lobster run *.lobster`) — a CLI that parses YAML step graphs and executes them sequentially with gates
- Hook engine — fires scripts inside the Gateway lifecycle on every message, session start, compaction

**You cannot import a runtime by copying files.** The lobster runner and hook engine are executables that live inside the OpenClaw process. Copying `.lobster` files to Hermes doesn't give Hermes the ability to run them.

---

## Capability Matrix

| Capability | OpenClaw (VPS/Linux) | OpenClaw (Windows) | Hermes (Windows) | Notes |
|---|---|---|---|---|
| **Lobster workflow runner** | ✅ Yes — native `lobster run` CLI | ❌ No | ❌ No | OpenClaw-specific executable; not portable |
| **Lobster workflow *definitions*** | ✅ Yes | ✅ Yes (at `claudecowork\orchestration\lobster\`) | ✅ Can author them | Definitions are YAML; execution requires runner |
| **Hook engine (event-driven)** | ✅ Yes — Gateway lifecycle hooks | ❌ No | ❌ No | Hooks fire inside OpenClaw Gateway process |
| **Hook *definitions*** | ✅ Yes | ✅ Yes (at `claudecowork\orchestration\hooks\`) | ✅ Can author them | Definitions are scripts; execution requires engine |
| **kanban.db (task claims/locks)** | ✅ Yes | ✅ Yes | ⚠️ Shared — conflicts if both write | OpenClaw's gateway process claims tasks; Hermes writing would conflict |
| **Cron jobs** | ✅ Yes | ✅ Yes (8 jobs at `hermes\cron\jobs.json`) | ✅ Yes | Hermes has 8 learning pipeline cron jobs |
| **Skill definitions** | ✅ Yes | ✅ Yes | ✅ Yes | All three platforms have skill directories |
| **Orchestration-loop skill** | ✅ Yes | ✅ Yes | ✅ Yes (`objective-orchestration-loop`) | Skill exists on all; only Hermes has actual enforcement guard |
| **Continuity files (file-based)** | ✅ Yes | ✅ Yes | ✅ Yes | All three have harness/CONTINUATION/KANBAN/WORK_LOG |
| **Enforcement heartbeat** | ✅ Via lobster + cron | ❌ None | ✅ `hermes_orchestration_guard.py` + cron | Hermes has actual heartbeat script; OpenClaw relies on lobster |

---

## Why "Import OpenClaw Into Hermes" Doesn't Work

### Scenario 1: Copy lobster files to Hermes
**Result:** Files exist. Hermes cannot run them.
**Why:** The lobster runner is a compiled binary inside OpenClaw's install at `/root/.openclaw/` on VPS. It's not a Python script or portable executable. Without the runner, lobster files are inert YAML.

### Scenario 2: Copy hook scripts to Hermes
**Result:** Scripts exist. Hermes cannot fire them.
**Why:** Hooks fire inside the OpenClaw Gateway's message-processing loop. The Gateway calls hook scripts at specific lifecycle points (message received, session start, step complete, compaction). Hermes has no equivalent event loop.

### Scenario 3: Let Hermes write to OpenClaw's kanban.db
**Result:** Both platforms write to the same SQLite DB.
**Why:** OpenClaw's gateway process holds locks on `tasks/runs.sqlite`. Concurrent writes from Hermes would cause database locks and corruption. The kanban enforcement only works because OpenClaw's own process is the sole writer.

### Scenario 4: Hermes calls OpenClaw's gateway API (port 18792)
**Result:** Possible but not useful.
**Why:** The gateway API is designed for OpenClaw's own agent runtime — sending it arbitrary tasks would not trigger lobster workflows or hooks. It's not a general-purpose enforcement API.

### Scenario 5: SSH to VPS and run `lobster run` from Hermes
**Result:** ✅ This works.
**Why:** The VPS has the lobster runner. If Hermes can SSH to `100.67.172.114`, it can run `lobster run *.lobster` commands remotely. The lobster files at `claudecowork\orchestration\lobster\` can be executed this way.
**Requirement:** VPS must be online. VPS was frequently down during May 2026.

---

## What Actually Works

### Option A: SSH to Linux PC (100.116.214.127) + run OpenClaw
```
ssh open-claw@100.116.214.127 "openclaw run --profile default"
```
- ✅ OpenClaw installed and verified (2026.5.7, eeef486)
- ✅ mcporter 0.7.3 available for TradingView Remix
- ✅ Non-interactive SSH works (bashrc fix applied 2026-05-16)
- ⚠️ Desktop machine — uptime depends on user session
- ❌ Cannot allocate PTY interactively from Hermes terminal tool

### Option B: SSH to VPS (100.67.172.114) + run lobster remotely
```
ssh root@100.67.172.114 "lobster run /root/openclawtrading/orchestration/lobster/hermes-task-closeout.lobster"
```
- ✅ Lobster executes on VPS with native runner
- ✅ Hooks fire inside OpenClaw Gateway on VPS
- ❌ VPS must be online
- ❌ Hermes is just driving OpenClaw remotely — not getting native enforcement

### Option B: Build a lobster runner for Hermes
Extract the lobster YAML parser + step executor from OpenClaw's open-source codebase and run it as a Python script in Hermes.
- ✅ Hermes gets native lobster execution
- ❌ Significant engineering project
- OpenClaw's lobster runner is not yet open source (as of May 2026)

### Option C: Hermes file-based enforcement (already built)
Hermes uses `CONTINUATION.md` + `KANBAN.md` + `WORK_LOG.md` + `hermes_orchestration_guard.py` (cron heartbeat) as the truth store instead of kanban.db locks.
- ✅ Works today
- ✅ Actual heartbeat enforcement
- ❌ No step-gate guarantees (lobster forces you through steps)
- ❌ No event-driven hooks

### Option D: Hermes consumes OpenClaw's lobster *definitions* via SSH
Author lobster files in Hermes `claudecowork\orchestration\lobster\` but execute them via SSH to the VPS.
- ✅ Hermes can author and maintain lobster workflow definitions
- ✅ OpenClaw's runner executes them
- ❌ Tight coupling — Hermes workflow depends on OpenClaw VPS
- ❌ VPS must be online

---

## Path Reference

| Asset | OpenClaw VPS (100.67.172.114) | OpenClaw Linux PC (100.116.214.127) | OpenClaw (Windows) | Hermes (Windows) |
|---|---|---|---|---|
| OpenClaw version | ~2026.3.x | 2026.5.7 ✅ | varies | N/A |
| Lobster runner | `/root/.openclaw/lobster` | Not present | Not present | Not present |
| Lobster files | `/root/openclawtrading/orchestration/lobster/` | `~/openclawtrading/orchestration/lobster/` | `claudecowork\\orchestration\\lobster\\` | `claudecowork\\orchestration\\lobster\\` |
| Hook definitions | `/root/openclawtrading/workspace/hooks/` | `~/openclawtrading/hooks/` | `claudecowork\\orchestration\\hooks\\` | `claudecowork\\orchestration\\hooks\\` |
| kanban.db | `/root/.openclaw/tasks/runs.sqlite` | `~/.openclaw/tasks/runs.sqlite` | `.openclaw\\tasks\\runs.sqlite` | Uses file-based KANBAN.md |
| Gateway port | 18792 | ~18792 | 18792 | N/A |
| Cron jobs | Via OpenClaw cron | Via user crontab | Via Hermes cron | `hermes\\cron\\jobs.json` |
| mcporter | ✅ via npm global | ✅ via npm global | `AppData\\Roaming\\npm\\mcporter` | `AppData\\Roaming\\npm\\mcporter` |
| Continuity files | In workspace | In workspace | In harness subdirectory | In harness subdirectory |
| SSH user | `root` | `open-claw` | N/A | N/A |
| SSH access | Tailscale 100.67.172.114 | Tailscale 100.116.214.127 | N/A | N/A |

---

## Decision Rule

When the user asks about combining OpenClaw and Hermes for enforcement:

1. **Is the VPS online?** → SSH + `lobster run` is the fastest path to real lobster execution
2. **Does Hermes need native step-gates?** → Build a lobster runner (major project) or accept file-based enforcement
3. **Is the question about workflow *definitions*?** → Author them in Hermes; execute via SSH to OpenClaw VPS
4. **Is the question about kanban enforcement?** → Hermes uses file-based kanban; OpenClaw uses kanban.db locks — they are incompatible for shared use
