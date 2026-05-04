---
description: Start a meaningful Chimera objective with the right route, workflow, and done contract
agent: chimera-plan
---

Run the orchestration precheck for this request.

Before anything else, run the shared task-transition guard:

- `powershell -ExecutionPolicy Bypass -File scripts/validate_task_transition.ps1 -Platform opencode`

If that guard fails:

- do not start the new meaningful task
- explain that shared GitHub coordination truth must be updated first
- return a blocked start instead of continuing anyway

Then produce a compact objective-start brief with:

- ultimate objective
- current slice
- orchestration decision
- orchestration class
- why this route fits
- workflow choice
- enforcement surface choice
- proof needed
- done contract
- receipt path
- next implementation step

If the work is meaningful, remind the build agent to use:

- `prompt-upgrade-engineer`
- `sal-communication-contract`
- `vibe-coding-operator`
- `objective-orchestration-loop`
- `hook-opportunity-detector` when the user wants something to auto-trigger
- `pipeline-enforcement-detector` when a recurring workflow owner is needed
