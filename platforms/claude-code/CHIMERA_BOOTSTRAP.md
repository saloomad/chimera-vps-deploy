# Claude Code Chimera Bootstrap

Read order:

1. this file
2. `AGENTS.md`
3. `skills/objective-orchestration-loop`
4. `skills/model-registry`
5. latest `handoffs/CHECKPOINT_*.md`

Platform truth:

- native home: `C:\Users\becke\.claude\`
- local skills: `C:\Users\becke\.claude\skills\`
- current provider selection depends on local Claude settings files

Rule:

- use the same plan execute review loop as the other platforms
- do not pretend Claude Code has durable background continuation if it does not
- use the shared hook bundle mirror under `platforms/claude-code/project-bundle/` when you need to recreate the local `.claude/` enforcement setup
