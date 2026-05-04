# Chimera OpenCode Bundle

This folder is the committed OpenCode project bundle for Chimera.

What it gives us:

- project-local commands in `.opencode/commands/`
- project-local prompts in `.opencode/prompts/`
- project-local native skills in `.opencode/skills/`
- a root `opencode.json` config that wires the Chimera agents and safer permissions

What it does not give us:

- a separately verified native hook API like Claude Code

So the OpenCode enforcement model here is:

1. project `AGENTS.md`
2. project `opencode.json`
3. project `.opencode/commands/*`
4. native skill discovery from `.claude/skills`, `.agents/skills`, and OpenCode skill homes
5. file-backed plans and review contracts when the task is multi-step
6. activation receipts through command and prompt driven logging when native hooks are not proven

Use this bundle for:

- orchestration precheck
- starter-stack reminders
- plan or build agent routing
- safer closeout behavior
