---
name: task-transition-publish
description: Publish shared task status before moving from one meaningful task to another, even when code is unfinished. Use when switching tasks, parking work, leaving a slice half-done, or telling another platform what still needs publishing. Triggers: switch tasks, move to next task, publish debt, unfinished work, before moving on.
---

# Task Transition Publish

Use this skill when a continuous session changes tasks.

## Core Rule

Task transition is the real publish boundary.

Before another meaningful task starts, the current task must leave behind shared truth.

## Choose One State

### Published Ready

Use when:

- code or artifact is tested enough
- the slice is ready to commit and push

Required actions:

- update `session-states/<platform>.yaml`
- push the correct repo
- update handoff when the slice matters cross-platform

### In Progress Not Ready

Use when:

- work moved forward
- code is still incomplete or untested
- another task still needs to start

Required actions:

- update `session-states/<platform>.yaml`
- update `publish-queue/<platform>.yaml`
- list local-only changes
- state the next action clearly

### Blocked Needs Follow-Up

Use when:

- a real blocker stopped progress
- safe continuation needs another owner, platform, or approval

Required actions:

- update `session-states/<platform>.yaml`
- update `publish-queue/<platform>.yaml`
- record the blocker and next owner

## Do Not Do This

- do not rely on chat memory
- do not leave the slice only in a private local file
- do not jump to a new task with no publish state

## Related Files

- `session-states/*.yaml`
- `publish-queue/*.yaml`
- `handoffs/CHECKPOINT_*.md`

---
*task-transition-publish v1.0 | 2026-05-04 | Chimera shared skill*
