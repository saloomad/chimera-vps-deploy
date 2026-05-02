# Workflow Catalog

Use this file to choose the right workflow loop for the task.

## Starter Stack

For meaningful software and workflow requests, start with:

1. `prompt-upgrade-engineer`
2. `sal-communication-contract`
3. `vibe-coding-operator`
4. `objective-orchestration-loop`

Add:

5. `major-build-council-orchestrator` when real tradeoffs exist
6. `vibe-coding-monitor` when friction, misses, or weak explanation appear

Communication rule:

- do not cite a file, commit, branch, workflow, or detector without explaining what it is and why it matters

## Workflow Categories

### 1. Direct Ask

- Use when: one bounded answer or tiny change
- Loop type: usually one-pass
- Main workflow: `skill-preflight-and-closeout.md`

### 2. Bounded Build

- Use when: build, fix, implement, refactor, or test work needs several steps
- Loop type: loop-until-done
- Main workflows:
  - `meaningful-change-lifecycle-and-enforcement-loop.md`
  - `vibe-coding-build-and-finish-loop.md`
  - `build-test-verify-monitor-closeout.md`

### 3. Major Build With Council

- Use when: architecture or system-wide tradeoffs exist, or the user asks for a council
- Loop type: council once, then loop-until-done delivery
- Main workflows:
  - `major-build-council-and-delivery-loop.md`
  - `OBJECTIVE_PLAN_TEMPLATE.md`

### 4. Project Start

- Use when: a new initiative or major workstream is beginning
- Loop type: usually bounded loop
- Main workflow:
  - `project-start-and-objective-intake-loop.md`

### 5. Project Finish

- Use when: finishing, shipping, handing off, or closing meaningful work
- Loop type: bounded closeout loop
- Main workflow:
  - `project-finish-and-delivery-loop.md`

### 6. GitHub Publish And Shared Sync

- Use when: branch, commit, push, PR, sync, or shared-skill mirror work is involved
- Loop type: bounded loop
- Main workflow:
  - `github-publish-and-shared-sync.md`

### 7. Dependency Update

- Use when: libraries, package versions, or tool dependencies change
- Loop type: bounded loop
- Main workflow:
  - `dependency-update-and-verification-loop.md`

### 8. Test Failure And Proof Repair

- Use when: proof is weak, tests are missing, or tests fail
- Loop type: loop until proof is honest
- Main workflow:
  - `test-failure-and-proof-repair-loop.md`

### 9. Workflow And Skill Promotion

- Use when: a pattern keeps repeating and should become reusable
- Loop type: one-pass promotion decision, then follow-up if needed
- Main workflows:
  - `reusable-pattern-capture.md`
  - `skill-workflow-mirror-and-publication.md`

### 10. PM And Front-Door Reconciliation

- Use when: tasks, reminders, or delivery/front-door surfaces may be stale or drifted
- Loop type: bounded reconciliation loop
- Main workflows:
  - `task-and-continuity-closeout.md`
  - project-operations-manager skill

### 11. Trading / Deezoh Lifecycle

- Use when: market classification, trade lifecycle, desk review, or operator brief work is needed
- Loop type: stateful loop
- Main workflows:
  - `deezoh-market-condition-and-trade-lifecycle-loop.md`
  - `openclaw-monitoring-and-consumer-loop.md`

## Rule

Every workflow should say whether it is:

- one-pass
- loop-until-done

If looped, it must define:

- objective contract
- review outcomes
- stop or escalation condition

For any meaningful system change, also define:

- enforcement surface
- dependent surfaces to update
- proof shape
- documentation and continuity update path
