# Claude Code Orchestration Hooks

This project-level Claude Code setup enforces the shared Chimera orchestration contract with native Claude hooks.

## Installed Hooks

- `UserPromptSubmit`
  - injects the orchestration precheck on every prompt
- `SessionStart`
  - reminds Claude of the active objective contract when a session starts or resumes
  - forces a shared coordination read of handoffs, session states, and publish queue
- `PreToolUse`
  - warns before meaningful edits or shell steps
  - blocks obviously destructive shell commands
- `PostToolUse`
  - nudges Claude to update proof and review state after edits or shell work
  - nudges Claude to update shared session state and publish debt when a slice moves
- `PostToolUseFailure`
  - nudges Claude to record failure and choose `iterate` or `blocked` honestly
- `SubagentStop`
  - forces a proof-minded integration review before trusting subagent output
- `Stop`
  - blocks stopping if `.claude/OBJECTIVE_CONTRACT.md` is still marked `status: active`
  - also blocks stopping when the objective contract is newer than the shared coordination files

## What This Enforces

- every meaningful request gets an orchestration precheck
- meaningful edits and shell steps get a workflow and proof reminder
- destructive shell commands are blocked instead of trusted
- failed tool steps are pushed back into the review loop
- subagent output must be reviewed before it is treated as final
- active objectives cannot be closed casually at the end of a reply
- a task cannot be abandoned locally without shared publish truth
- meaningful replies should carry forward objective status, unapproved items, and remaining work in one short visible block
- shared coordination skills should be loaded when startup or task-transition publish logic matters
- task-change-readiness-gate should be treated as the final permission check before a new meaningful task starts
