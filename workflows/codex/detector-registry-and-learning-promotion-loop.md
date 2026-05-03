# Detector, Registry, And Learning Promotion Loop

Use this workflow when a session reveals:

- a repeated pattern that should become a workflow
- a repeated behavior gap that should become a skill
- a repeated event reminder that should become a hook
- a runtime ownership problem that should be moved to Task Flow, Lobster, standing orders, commands, or review gates
- a durable lesson that should help future Chimera work or other projects

## Loop Type

- one-pass promotion decision, then bounded follow-through

## Trigger Points

- `PreToolUse`
  - when a risky or control-layer change reveals a missing workflow, skill, or hook
- `SubagentStop`
  - when a subagent result reveals a reusable pattern, weak proof shape, or missing runtime owner
- `PostToolUse`
  - when a meaningful change landed and should update the registries or learning surfaces
- `Stop`
  - before closeout when the session produced durable lessons or repeated friction

## Skills To Use

1. `codex-workflow-detector`
2. `codex-skill-opportunity-detector`
3. `hook-opportunity-detector`
4. `pipeline-enforcement-detector` when recurring ownership or trading/runtime state is involved
5. `codex-feature-opportunity-detector` when the right answer may be a platform-native feature
6. `codex-lesson-harvester`
7. `cross-project-ai-lessons` when the lesson is useful outside Chimera

## Required Checks

1. confirm the pattern is real, not a one-off
2. decide whether the missing thing is:
   - a workflow
   - a skill
   - a hook
   - a runtime owner
   - a durable lesson
3. check whether an existing workflow, skill, or platform feature already covers it
4. choose the smallest honest fix
5. update the registries and inventories
6. update continuity or handoff surfaces if the lesson matters later

## Required Outputs

- what pattern was detected
- what existing surface was checked first
- what was created or updated
- what platform should enforce it
- why that enforcement choice fits
- what is still missing
- what future projects can reuse
