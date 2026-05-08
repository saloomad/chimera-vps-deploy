# CHECKPOINT_2026-05-05_workspace_navigation_registry_finalization

## What landed

- the workspace navigation stack now has a shorter canonical route:
  - `AGENT_SITUATION_ROUTER.md`
  - `AGENT_NAVIGATION_MAP.md`
  - `WORKSPACE_FILE_OPERATING_RULES.md`
  - `WORKFLOW_MAP.md`
  - `tasks/TASK_REGISTRY.md`
  - `DOCUMENT_REGISTRY.md`
- `WORKFLOW_MAP.md` is now the canonical workflow front door and explicitly points to `workflows/codex/WORKFLOW_CATALOG.md`
- `tasks/TASK_REGISTRY.md` is now the canonical task surface
- root `TASK_REGISTRY.md` is now a reference-only redirect
- `OPENCLAW_FILE_MAP.md`, `OPENCLAW_BIBLE.md`, and `OPENCLAW_FEATURES.md` are now reference-only helper docs instead of competing front doors
- `WORKSPACE_FILE_OPERATING_RULES.md` and `AGENT_NAVIGATION_MAP.md` now include a topic-to-owner update/create matrix
- `scripts/build_workspace_document_registry.py` was hardened to:
  - demote or exclude noisy mirror/artifact roots from the main human registry view
  - add `AGENT_SITUATION_ROUTER.md`, `WORKFLOW_MAP.md`, and `tasks/TASK_REGISTRY.md` as first-class front doors
  - generate a shorter `INDEX.md`
  - keep registry docs from recursively self-reporting their own legacy-warning tables
- `tracking/REDUNDANT_FILE_REVIEW.md` now includes class-based demotion rules for imported mirrors, runtime stores, screenshot roots, scratch docs, and usage artifacts
- wiki capture was added for this pass:
  - `research/chimera-knowledge-wiki/wiki/sources/workspace-navigation-and-registry-hardening-2026-05-05.md`

## Proof

- local registry rebuild:
  - `Registry updated: 5453 tracked files`
- local wiki health:
  - `in_index_not_on_disk = []`
  - `on_disk_not_in_index = []`
- live VPS registry rebuild:
  - `Registry updated: 3694 tracked files`
- live VPS `INDEX.md` now starts with:
  - `Read This By Situation`
  - `AGENT_SITUATION_ROUTER.md`
  - `WORKFLOW_MAP.md`
  - `tasks/TASK_REGISTRY.md`
- hash proof matched for key mirrored files:
  - `AGENT_SITUATION_ROUTER.md`
  - `WORKFLOW_MAP.md`
  - `scripts/build_workspace_document_registry.py`
  - `tracking/WORKSPACE_FILE_REGISTRY.md`
  - `research/chimera-knowledge-wiki/wiki/sources/workspace-navigation-and-registry-hardening-2026-05-05.md`

## Council result

The critique from both background reviewers was implemented in the final pass:

- reduce registry noise from imported mirrors and artifact roots
- make workflow routing singular
- make task routing singular
- demote older `OPENCLAW_*` docs to reference-only
- add a faster update-vs-create matrix
- move `INDEX.md` away from full census behavior

No higher-value structural improvement remained for this slice after the final rebuild and live mirror proof.

## Remaining optional cleanup

- continue the separate legacy-root-doc modernization lane for older root files that still have `/home/open-claw/...` or other retired path references
- if desired later, further tighten `DOCUMENT_REGISTRY.md` category sections so they stay almost entirely front-door oriented and not mixed with secondary active docs
