# Critical Config, Instruction, And Compaction Guard Loop

## Trigger

Use this workflow when the change touches the control layer rather than normal feature code.

Examples:

- `AGENTS.md`
- `CLAUDE.md`
- startup docs
- shared instructions
- plugin or app config
- `opencode.json`
- `.claude/settings.json`
- OpenCowork plugin registry or local plugin bundle
- skill files
- workflow files
- detector files
- compaction-before or compaction-after continuity behavior
- PM or continuation files that decide how later sessions resume

If the change could alter how future agents behave, route, explain, continue, or stop, this workflow applies.

## Purpose

This is the safe loop for risky control-layer changes.

It exists to stop agents from casually editing instructions, hooks, config, or continuity surfaces without:

- choosing the right workflow
- choosing the right enforcement surface
- planning backup and rollback
- testing the real startup or continuation behavior
- updating dependent docs, PM, and continuity surfaces

## Required Companion Skills

1. `critical-change-guard`
2. `objective-orchestration-loop`
3. `sal-communication-contract`
4. `codex-continuity-enforcer`

Add when needed:

- `hook-opportunity-detector`
- `codex-workflow-detector`
- `codex-skill-opportunity-detector`
- `pipeline-enforcement-detector`
- `project-operations-manager`

## Inputs

- objective
- current control-layer surface
- target platform
- risk level
- affected files
- expected startup, hook, compaction, or continuation behavior
- proof path

## Ordered Steps

### 1. Classify the control-layer change

Say which kind of change this is:

- instruction change
- config change
- hook change
- workflow change
- skill change
- detector change
- continuity or PM change
- compaction governance change

### 2. Run critical pre-flight

Before editing:

- define objective
- define risk
- define affected platforms
- define backup path
- define rollback path
- define tests
- define the honest review boundary

Use `critical-change-guard`.

### 3. Choose the workflow owner

Pick the main owner:

- startup rule
- hook
- workflow
- skill
- detector
- command
- permission gate
- Task Flow
- Lobster
- standing order
- scheduler
- monitor

If the owner is unclear, use `platform-enforcement-selection-and-receipt-loop.md`.

### 4. Name the dependent surfaces

Before editing, list what else will probably need updating:

- shared instructions
- mirrored platform copies
- workflow catalog
- enforcement inventory
- PM or continuity files
- research or wiki notes
- verifier scripts
- receipt paths

### 5. Implement the smallest honest change

- keep the write scope clear
- avoid mixing unrelated cleanup
- if the change is platform-specific, say which platform owns it

### 6. Protect continuity around compaction

If the session may compact, split, or hand off:

- capture current objective state
- capture current PM state
- capture current continuation state
- capture proof paths
- capture next step and stop condition

Use:

- `task-and-continuity-closeout.md`
- `codex-continuity-enforcer`

### 7. Test the behavior

Use the strongest realistic proof:

- file proof
- startup proof
- hook proof
- receipt proof
- compaction continuity proof
- live platform pickup proof

For control-layer changes, do not stop at "the file exists."

### 8. Review control-layer risk

Answer:

- did the enforcement path really get wired
- did continuation get protected
- did PM state stay truthful
- did startup or compaction behavior improve
- did the proof actually test the risky behavior
- is the result `complete`, `iterate`, or `blocked`

### 9. Document and sync

Update the smallest truthful set of:

- workflow catalog
- enforcement inventory
- relevant skills
- PM or continuity files
- research or wiki notes
- shared mirrors

## Expected Outputs

- updated control-layer surface
- named enforcement owner
- proof result
- continuity update
- PM update when needed
- updated docs or inventory
- honest review outcome
