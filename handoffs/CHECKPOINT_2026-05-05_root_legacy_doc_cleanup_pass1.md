# CHECKPOINT_2026-05-05_root_legacy_doc_cleanup_pass1

## What landed

This follow-up pass continued after the workspace navigation finalization and targeted active root docs that still taught retired runtime/path truth.

Patched:
- `AGENT_OPTIMIZATION.md`
- `LEAD_WORKFLOW.md`
- `PIPELINE_MAP.md`
- `OPENCLAW_HOOKS.md`

What changed:
- `LEAD_WORKFLOW.md` is now a reference-only redirect to the current workflow front doors
- `PIPELINE_MAP.md` is now a reference-only historical pipeline note
- `OPENCLAW_HOOKS.md` is now a reference-only hook overview that routes to the current registry/runtime proof surfaces
- `AGENT_OPTIMIZATION.md` keeps its optimization guidance, but its old hardcoded Linux paths were replaced with current relative/current-truth references

## Proof

- local literal retired-path scan on the four targeted docs returned no:
  - `/home/open-claw`
  - `192.168.1.203`
  - `100.116.214.127`
  - `192.168.31.194`
  - `open-claw@192.168.1.203`
- local registry rebuild completed through the background run:
  - `Registry updated: 5478 tracked files`
- local `DOCUMENT_REGISTRY.md` legacy count dropped:
  - before slice: `1212`
  - after slice: `1204`
- live VPS registry rebuild completed:
  - `Registry updated: 3721 tracked files`
- live VPS `DOCUMENT_REGISTRY.md` now shows:
  - `files with legacy runtime references: 43`

## Practical meaning

- the navigation/front-door system remains the main canonical layer
- the next cleanup work is no longer structural front-door confusion
- it is now a narrower legacy-root-doc rewrite lane

## Remaining optional cleanup

- continue through the next active root docs still listed in local `DOCUMENT_REGISTRY.md` legacy warnings, for example:
  - `COMMUNICATION_PROTOCOL_v2.md`
  - `COMMUNICATION_PROTOCOL_v3.md`
  - `CONTINUATION_ARCHIVE.md`
  - `CROSS_PLATFORM_ANALYSIS.md`
  - `DAILY_LOG.md`
  - `KANBAN.md`
  - `MEMORY_GUIDE.md`
  - `MEMORY_OPTIMIZATION.md`
