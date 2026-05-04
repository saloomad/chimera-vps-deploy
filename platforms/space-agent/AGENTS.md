## Space Agent Chimera Instructions

Space Agent is the visual and browser-first Chimera lane.

## Read first before meaningful work

1. `C:\Users\becke\claudecowork\shared_ai_context\PROJECT_GOALS.md`
2. `C:\Users\becke\claudecowork\shared_ai_context\CURRENT_STATE.md`
3. `C:\Users\becke\claudecowork\shared_ai_context\NEXT_ACTIONS.md`
4. `C:\Users\becke\claudecowork\shared_ai_context\TASKS_LEFT.md`
5. `C:\Users\becke\claudecowork\research\INDEX.md`
6. `C:\Users\becke\claudecowork\chimera-vps-deploy\platforms\space-agent\SHARED_CONTEXT_README.md`

## Default role

- use Space Agent for dashboards, visual operator surfaces, browser-first workspaces, and UI-facing coordination
- do not treat Space Agent as the main source of project truth
- use the shared context as the startup default before visual work begins

For meaningful workflow, UX, dashboard, or coordination work, use the same starter stack in lighter form:

1. `prompt-upgrade-engineer`
2. `sal-communication-contract`
3. `vibe-coding-operator`
4. `objective-orchestration-loop`

If the session shows friction or weak operator guidance:

5. `vibe-coding-monitor`

If architecture or system-wide tradeoffs exist:

6. `major-build-council-orchestrator`
7. `github-coordination-gate`
8. `task-transition-publish`
9. `platform-live-repo-router`
10. `task-change-readiness-gate`

For meaningful replies, use `sal-communication-contract` so visual or workflow updates still explain the practical meaning of files, steps, and proof.

For any meaningful create, build, fix, refactor, workflow change, skill change, or automation change, also use the shared change lifecycle workflow and the platform hooks matrix.

## Task-Switch Gate Reality

This platform does not currently have a separately versioned native hook or command bundle in this repo that can hard-deny a new task the way Claude Code or OpenClaw can.

So the strongest truthful rule here is:

1. treat `github-coordination-gate`, `task-transition-publish`, `platform-live-repo-router`, and `task-change-readiness-gate` as mandatory
2. before leaving one meaningful task for another, run the shared guard from the Windows workspace:
   - `python C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\github_coordination_guard.py validate-platform --coordination-root C:\Users\becke\claudecowork\chimera-vps-deploy --platform opencode`
3. if that guard fails, do not move on

Be honest that this is a wrapper rule, not a separately proven native Space Agent hard-stop API.

## Continuity rule

If a Space Agent session learns something durable:

- save research under `C:\Users\becke\claudecowork\research\`
- update `shared_ai_context\` if project truth changed
- prefer canonical docs over standalone visual-only notes

The shared Chimera knowledge wiki lives at:

- `C:\Users\becke\claudecowork\research\chimera-knowledge-wiki`

Read it before visual work when prior research, build lessons, workflow guidance, or architecture context would shape the UI work.

Update it when a Space Agent session produces durable visual, workflow, or architecture knowledge that should survive the session.

Use it as the durable research layer behind visual work, not as live runtime truth.
Also use the shared coordination repo before changing meaningful UI or coordination tasks.
