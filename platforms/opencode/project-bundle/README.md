# Chimera OpenCode Bundle

This folder is the committed OpenCode project bundle for Chimera.

What it gives us:

- project-local commands in `.opencode/commands/`
- project-local prompts in `.opencode/prompts/`
- project-local native skills in `.opencode/skills/`
- a root `opencode.json` config that wires the Chimera agents and safer permissions
- a local task-transition wrapper at `scripts/validate_task_transition.ps1`

What it does not give us:

- a separately verified native hook API like Claude Code

So the OpenCode enforcement model here is:

1. project `AGENTS.md`
2. project `opencode.json`
3. project `.opencode/commands/*`
4. native skill discovery from `.claude/skills`, `.agents/skills`, and OpenCode skill homes
5. file-backed plans and review contracts when the task is multi-step
6. activation receipts through command and prompt driven logging when native hooks are not proven

The strongest task-switch wrapper we can prove here is:

1. use `objective-start` before a new meaningful task
2. run `scripts/validate_task_transition.ps1` first
3. refuse the task start if the shared coordination guard fails

This is stronger than docs alone, but still not the same thing as a native hook-deny API.

Use this bundle for:

- orchestration precheck
- starter-stack reminders
- plan or build agent routing
- safer closeout behavior
