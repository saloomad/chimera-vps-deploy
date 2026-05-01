---
name: system-change-verifier
description: Verify that a new change works across local checks, producer-consumer integration, workflow behavior, bounded live proof, and monitoring or handoff instead of treating file creation as completion.
triggers:
  - verify this change
  - does this really work
  - integration test
  - prove this works
  - whole system
  - dependency check
  - consumer check
---

# System Change Verifier

Use this skill when a change claims to work end-to-end, especially if it touches more than one script, report, agent, workflow, or runtime surface.

## Read First

- `workflows/codex/build-test-verify-monitor-closeout.md`
- `docs/CRITICAL_CHANGE_PROTOCOL.md`
- `docs/LEAD_ENGINEERING_PLAYBOOK.md`
- `tasks/TASK_REGISTRY.md`
- the changed files

## Verification Matrix

For each change, check the smallest truthful set of:

1. syntax or build checks
2. local functional checks
3. producer-consumer contract checks
4. workflow or operator-surface checks
5. bounded live proof when reachable
6. monitoring or handoff need
7. remaining gaps

## Important Rules

- File existence is not integration proof.
- Passing one local test is not whole-system proof.
- If the live layer was not tested, say so clearly.
- If a dependency or consumer is missing, log that explicitly instead of calling the change done.

## Write Targets

- `docs/` for proof or audit reports
- `tasks/TASK_REGISTRY.md`
- `trace/ACTION_LOG.md`
- continuity files when the verification result affects later work

## Success Condition

The output should end with one of these honest states:

- built and proven
- built and partially proven
- built but integration not yet proven
- blocked before proof
