# Markdown Artifact Governance And Closeout Loop

Use this workflow whenever an agent creates or updates a meaningful `.md` file.

Examples:

- instructions
- architecture docs
- skill docs
- workflow docs
- registries
- PM or continuity files
- reports and handoffs
- improvement backlogs

## Loop Type

- bounded loop

## Why This Exists

Markdown work often turns into dead-end documentation:

- a file gets created
- nobody explains what it means
- nobody updates the related registries
- other platforms do not get mirrored
- no hook, workflow, or follow-up uses it later

This workflow exists to stop that.

## Required Steps

1. classify the markdown artifact:
   - instruction
   - workflow
   - skill doc
   - architecture doc
   - PM or continuity doc
   - registry
   - report or handoff
   - improvement backlog
2. explain in plain English what was created or changed
3. decide whether the artifact changes system behavior or is only descriptive
4. if it changes behavior, choose the enforcement surface:
   - instruction
   - skill
   - workflow
   - hook
   - command
   - review gate
   - runtime owner
5. update the related registries:
   - workflow catalog
   - skills available
   - enforcement inventory
   - global registry
6. mirror to other platforms when the artifact matters outside local Codex
7. decide whether a detector or learning skill should also run
8. leave a clear next-use rule:
   - who should read this
   - when it should be used
   - how it avoids becoming dead documentation

## Skills To Use

- `sal-communication-contract`
- `response-structure-enforcer`
- `codex-workflow-detector`
- `codex-skill-opportunity-detector`
- `hook-opportunity-detector`
- `codex-lesson-harvester`

## Required Output

- what the markdown file is
- why it was needed
- what system behavior it changes, if any
- what other files were updated so it will actually be used
- what is still missing
