# Global Platform Skill, Workflow, And Hook Registry

Updated: 2026-05-03

## What This Is

This is the simplest global map of:

- what hooks should enforce
- when skills should load
- when workflows should be mandatory
- which platform should own the behavior
- what we already have
- what is still missing
- what lessons are reusable in other projects

## Global Starter Stack

Use this stack for meaningful software work unless the task is truly tiny:

1. `prompt-upgrade-engineer`
2. `sal-communication-contract`
3. `vibe-coding-operator`
4. `objective-orchestration-loop`

Add:

- `vibe-coding-monitor`
  - when friction, weak proof, confusion, or repeated correction appears
- `major-build-council-orchestrator`
  - when real system tradeoffs exist
- `hook-opportunity-detector`
  - when a repeated reminder should become event-driven
- `pipeline-enforcement-detector`
  - when a workflow needs a stronger runtime owner

## Event-To-Enforcement Logic

### `UserPromptSubmit`

Use for:

- prompt shaping
- workflow choice
- objective contract choice
- deciding whether the starter stack must load

Should load or check:

- `prompt-upgrade-engineer`
- `vibe-coding-operator`
- `objective-orchestration-loop`
- `major-build-council-orchestrator` when tradeoffs are real

### `PreToolUse`

Use for:

- risky command guardrails
- mutating file guardrails
- control-layer edits
- checking whether we picked the right workflow before acting

Should load or check:

- starter stack when a mutating action starts meaningful work
- `critical-change-guard` plus `critical-config-instruction-and-compaction-guard-loop.md`
  - when editing instructions, config, hooks, skills, workflows, detectors, continuity, or PM surfaces
- `hook-opportunity-detector`
  - when the same pre-action reminder keeps repeating
- `pipeline-enforcement-detector`
  - when the touched files suggest trading, Task Flow, Lobster, standing orders, Hermes runtime, or other recurring automation ownership

### `PostToolUse`

Use for:

- proof reminders
- dependent-surface reminders
- registry updates
- continuity and PM follow-through

Should load or check:

- `system-change-verifier`
- `project-operations-manager`
- `codex-workflow-detector`
- `codex-skill-opportunity-detector`
- `hook-opportunity-detector`
- `codex-lesson-harvester`

### `SubagentStop`

Use for:

- reviewing whether the subagent actually solved the assigned slice
- checking quality of proof, file list, tests, risks, and residual gaps
- deciding whether the result should promote a workflow, skill, hook, runtime owner, or lesson

Should load or check:

- `codex-workflow-detector`
- `codex-skill-opportunity-detector`
- `hook-opportunity-detector`
- `pipeline-enforcement-detector` when runtime ownership is involved
- `codex-lesson-harvester`
- `cross-project-ai-lessons` when the lesson should help other projects

### `Stop`

Use for:

- blocking premature closeout
- forcing `complete`, `iterate`, or `blocked`
- forcing proof and continuity closeout
- making sure the session does not throw away durable lessons

Should load or check:

- `objective-orchestration-loop`
- `vibe-coding-monitor`
- `project-operations-manager`
- `codex-lesson-harvester`
- `cross-project-ai-lessons`

### `PreCompact` and `PostCompact`

Use for:

- preserving the objective
- preserving the current slice
- preserving proof and PM state
- restoring a clear resume path

Should load or check:

- `codex-continuity-enforcer`
- `project-operations-manager` when PM state changed
- `codex-lesson-harvester` if the compaction boundary exposed a reusable continuity lesson

## When To Check For Existing Workflows Or Skills First

Always check for an existing workflow, skill, or platform feature first when:

- the same step sequence has already appeared twice
- the same explanation fix keeps being needed
- the same risky event keeps needing a reminder
- the same runtime pipeline ownership question comes up again
- the same lesson would obviously help the next session or another project

Main detectors:

- `codex-workflow-detector`
- `codex-skill-opportunity-detector`
- `hook-opportunity-detector`
- `pipeline-enforcement-detector`
- `codex-feature-opportunity-detector`

## Platform Ownership Logic

### Windows Codex

Best for:

- planning
- implementation
- explanation
- continuity
- research and documentation

Enforce with:

- `AGENTS.md`
- skills
- workflows
- thread heartbeats

### Claude Code

Best for:

- hook-based prechecks
- risky action guardrails
- stop gates
- subagent review

Enforce with:

- native hooks
- `CLAUDE.md`
- local hook scripts

### OpenCode

Best for:

- project rules
- commands
- prompts
- agents
- permissions

Enforce with:

- `opencode.json`
- `.opencode/*`
- commands, prompts, and review gates

Current limit:

- no separately proven native hook API in this workspace yet

### OpenCowork

Best for:

- local desktop plugin hooks
- local desktop commands
- local local-skill bundles

Enforce with:

- `%AppData%\\open-cowork\\claude\\plugins`
- `%AppData%\\open-cowork\\claude\\skills`
- local plugin registry

Current limit:

- bundle is enabled in the registry, but a real in-app session trigger is still the stronger missing proof

### OpenClaw / Kimi VPS

Best for:

- live runtime automation
- trading ownership
- restart-safe recurring workflows

Enforce with:

- hooks
- Task Flow
- Lobster
- standing orders
- scheduler wake-ups

### Hermes

Best for:

- runtime bridge outputs
- scheduled proofs
- paper-only bounded lanes

Enforce with:

- bridge scripts
- shared instructions
- receipt logging

## Registries We Have Now

- workflow catalog:
  - `workflows/codex/WORKFLOW_CATALOG.md`
- enforcement catalog:
  - `docs/PLATFORM_WORKFLOW_AND_SKILL_ENFORCEMENT_CATALOG_2026-05-02.md`
- hook and platform matrix:
  - `docs/PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-02.md`
- enforcement inventory:
  - `docs/ENFORCEMENT_IMPLEMENTATION_INVENTORY_2026-05-02.md`
- shared skills list:
  - `shared_ai_context/SKILLS_AVAILABLE.md`

## What Is Still Missing

- one clean proof of a real OpenCowork in-app session firing the local hooks
- stronger OpenCode auto-trigger proof if a real hook surface exists there
- stronger Task Flow runtime proof on OpenClaw
- a more explicit global workflow register mirrored to every platform startup surface

## What Other Projects Can Reuse

- keep `exists`, `wired`, `used`, and `verified live` separate
- use hooks for event checks, not for owning long-running state
- use a runtime owner like Task Flow or Lobster for recurring stateful pipelines
- treat control-layer changes as a special governed workflow
- treat `SubagentStop` and `Stop` as review gates, not as passive notifications
- keep one global registry plus one platform-specific inventory so people can learn the system without reading raw code first
