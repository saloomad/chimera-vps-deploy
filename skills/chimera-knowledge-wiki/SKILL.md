---
name: chimera-knowledge-wiki
description: Create, maintain, and use the Chimera knowledge wiki across platforms for market theses, operating intelligence, and contradiction tracking without confusing it with live runtime truth.
---

# Chimera Knowledge Wiki

Use this skill when the work is about:

- market and strategy research memory
- general research across tools, products, models, and outside topics
- build notes, implementation patterns, and project learnings
- skills, workflows, and platform operating guidance
- exchange docs and provider docs
- meeting notes and architecture decisions
- tool evaluations
- contradiction tracking across research inputs
- cross-platform knowledge capture that should outlive chat

## Core Rule

This wiki is for durable knowledge, not live runtime truth.

Allowed:

- research synthesis
- build and implementation memory
- skill and workflow memory
- operating documentation
- contradiction tracking
- saved answers
- cross-source linking

Not allowed as primary truth:

- live trade state
- fresh paper-watch truth
- live cron or service state
- front-door reminder truth

## Shared Template

The shared workspace template lives at:

- `C:\Users\becke\claudecowork\chimera-vps-deploy\research\chimera-knowledge-wiki-template`

Default installed workspaces:

- Windows:
  - `C:\Users\becke\claudecowork\research\chimera-knowledge-wiki`
- VPS:
  - `/root/openclawtrading/research/chimera-knowledge-wiki`

## Setup

Preferred scripts:

- Windows:
  - `chimera-vps-deploy/scripts/install_chimera_knowledge_wiki.ps1`
- Linux/VPS:
  - `chimera-vps-deploy/scripts/install_chimera_knowledge_wiki.sh`

These scripts should:

- copy the shared template into the target workspace
- preserve existing wiki content when re-run
- optionally install Python dependencies

## Default Workflows

### Ingest

Put sources into:

- `raw/market_thesis/`
- `raw/operating_intel/`
- `raw/build_and_skills/`
- `raw/general_research/`
- `raw/contradiction_watch/`

Then ingest with the agent or:

```bash
python tools/ingest.py <path>
```

### Health

Cheap automatic check:

```bash
python tools/health.py --json
```

### Lint

Slower semantic check:

```bash
python tools/lint.py --save
```

### Graph

Deterministic default:

```bash
python tools/build_graph.py --no-infer
```

## Automatic Maintenance Pattern

Use this pattern for recurring upkeep:

1. run `health.py`
2. run `catalog.py` and prefer catalog-first lookup before opening many pages
3. run `focus_audit.py --save` to catch oversized curated pages
4. if wording differs from saved page wording, use `semantic_search.py`
5. if new sources were added, rebuild the deterministic graph
6. run `lint.py --save` on a slower cadence or after batches
7. do not auto-ingest arbitrary live runtime files

## Read And Update Rule

Read this wiki early when:

- the task depends on prior research, prior architecture decisions, or prior build lessons
- the task touches skills, workflows, or cross-platform operating guidance
- the same topic has likely been explored before and chat memory would be fragile

Update this wiki during closeout when:

- a new durable lesson was learned
- a build or implementation pattern should be reusable later
- a skill, architecture decision, or research conclusion materially changed
- two sources were found to conflict and that contradiction should be preserved
- a repeated interaction pattern between Sal and the agents should become reusable guidance
- a vibe-coding, prompt-engineering, orchestration, or skill-routing lesson should survive the session

Do not wait for a human to explicitly ask for capture when the new knowledge is clearly durable and belongs in the shared research layer.

For vibe-coding and workflow-improvement work, prefer:

- `raw/build_and_skills/`
- wiki source pages under `wiki/sources/`
- links back to the related skill, workflow, and platform instruction surfaces

## Enforcement Reality

Current enforcement is a mix of:

- shared skill instructions
- platform-specific AGENTS/bootstrap guidance
- recurring health and graph maintenance
- recurring focus and capture audits
- shared install paths across platforms

Current enforcement is not yet:

- a hard OS-level write hook on every chat turn
- a guaranteed auto-read on every external platform session

So the intended behavior is strongly guided and increasingly automated, but still partly instruction-driven rather than absolute.

## Platform Optimization

The core logic is shared, but the surfaces differ:

- Codex and Claude-family tools can use the local skill directly
- OpenCowork uses its local Claude-style skill home
- OpenCode currently relies more on config plus docs, even though the skill files are mirrored there
- Kimi/OpenClaw/Hermes use mirrored skill homes on the VPS
- Space Agent is mainly a consumer and visual layer, not the main mutation owner

## Cross-Platform Goal

This skill should be installed across Codex, Claude-family tools, Kimi, Hermes, and other shared Chimera surfaces so each platform can operate the same workspace model.
