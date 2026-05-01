# Skill Preflight And Closeout

## Trigger

Use this workflow before any non-trivial task starts and again before meaningful work is called complete.

## Inputs

- current request
- current task context
- relevant repo-local skills and workflows
- changed files or systems

## Preflight Steps

1. Scan the request for matching repo-local skills, overlapping existing skills, and relevant workflows.
2. Choose the smallest useful set.
3. Tell Sal in one short line which skills you are using and why.
4. Use the chosen skills without waiting, unless the task hits an approval boundary.

## Closeout Steps

1. Run `system-change-verifier` if behavior changed or integration was claimed.
2. Run `monitoring-opportunity-detector` if the result can drift or fail silently later.
3. Run `codex-task-and-project-capture` if new follow-up work appeared.
4. Run `codex-continuity-enforcer` after meaningful work.
5. Run `codex-lesson-harvester` when the work taught a reusable lesson.
6. If you will claim a skill, workflow, hook, instruction layer, setup, or test exists or was used, capture the exact file path and the exact proof command/check result before replying.
7. If no extra skill applies, say so explicitly.

## Expected Outputs

- clear skill selection at the start
- clear closeout discipline at the end
- no hidden "auto-triggered" claims without evidence
- no vague setup/testing claims without file-path proof and verification detail
