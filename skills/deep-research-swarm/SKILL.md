---
name: deep-research-swarm
description: Run a specialized seven-phase research swarm for deep evidence gathering, cross-verification, synthesis, and writing. Use for heavy research, market theses, postmortems, and large comparisons. Do not use as the default loop for every trading cycle or normal coding task.
triggers:
  - deep research
  - research swarm
  - market thesis
  - weekly thesis
  - postmortem
  - cross verify
  - large comparison
---

# Deep Research Swarm

Use this skill only when the task is research-heavy enough to justify a specialized swarm.

This skill is a companion to `objective-orchestration-loop`, not a replacement for it.

## Use This When

- the job needs broad evidence gathering
- the topic has several meaningful dimensions
- the answer needs contradiction handling, not just summary
- the user wants a thesis, memo, report, or postmortem
- the job is too large for one linear read-and-write pass

## Do Not Use This When

- the task is a normal coding objective
- the task is a routine trading cycle
- the task is a one-step monitor or repair
- the task is already bounded enough for a simple plan execute review loop

## Core Principle

Parallel workers do not share memory.
Use files or explicit state handoffs as the source of truth.

Every worker should be given:

1. mission
2. context
3. exact output target

## The Seven Phases

### 1. Landscape Scan

The orchestrator gathers broad context and resets the time horizon.

Output should state:

- date and freshness window
- broad market or topic picture
- open tensions
- candidate dimensions

### 2. Dimension Decomposition

Break the problem into dimensions that are:

- meaningfully different
- still overlapping enough for cross-verification
- individually bounded

Dimension examples:

- timeframe
- stakeholder
- evidence source
- scenario or risk case
- sector or sub-market
- technical versus fundamental angle

### 3. Parallel Deep Dive

Launch one worker per dimension.

Each worker should:

- gather evidence
- cite or name the proof source when available
- separate strong findings from weak findings
- write partial output even if incomplete

Cheap worker rule:

- start dimension workers on the cheaper route first
- only rerun failed or ambiguous dimensions on a stronger lane

### 4. Cross-Verification

The verifier reads the dimension outputs and sorts findings into:

- high confidence
- medium confidence
- low confidence
- conflict zone

Contradictions are signal, not noise.

### 5. Targeted Validation

Only launch this phase if the conflict zone or weak evidence matters to the final answer.

Validation should be narrow:

- rerun only the failed dimension
- ask only the missing question
- use stronger reasoning only where needed

### 6. Insight Extraction

The orchestrator or synthesizer pulls out:

- cross-dimensional patterns
- tensions that survived validation
- action-relevant conclusions
- what remains unproven

### 7. Writing Pipeline

Writing is separate from research.

The writing phase should:

- preserve evidence and uncertainty
- organize the output for the user
- avoid silently inventing certainty

## Quality Gates

Use pass fail gates between phases.

Minimum examples:

- all required dimension outputs exist
- outputs meet a minimum completeness bar
- cross-verification explicitly records conflicts
- targeted validation resolves or preserves important uncertainty
- final writing does not skip the conflict zone

If a gate fails:

- rerun only the failed slice
- do not restart the whole swarm by default

## Model Routing

Read `codex-runtime-router` and `model-registry` first when the exact route matters.

Default split:

- orchestrator: strongest planning lane
- verifier: stronger review lane
- final synthesizer: stronger review or planning lane
- dimension workers: cheap execution lane first

Suggested defaults in this ecosystem:

- architecture analysis and orchestration design: `gpt-5.5` with `high`
- planning and workflow specification: `gpt-5.5` with `high` or `xhigh`
- local skill or document implementation: `gpt-5.4` with `medium`
- cheap workers: `gpt-5.3-codex-spark` with `low` or `gpt-5.4-mini` with `low`
- judgment-heavy review: `gpt-5.5` with `high`
- VPS live execution: `MiniMax-M2.7-highspeed`
- VPS rerun when the first result is weak: `k2.6` with thinking on

## Trading Pipeline Rule

Do not use this full swarm on every live trading cycle.

Use it for:

- weekly BTC or market theses
- major event-driven setup reviews
- deep ambiguity that needs cross-verification
- post-trade failure analysis
- large token or sector comparisons

Do not use it for:

- the routine setup watcher
- position management loops
- every five-minute or fifteen-minute market wake

## Expected Deliverables

A good swarm closeout should leave:

- a landscape note
- a dimension list
- dimension outputs
- a cross-verification note
- a targeted-validation note when needed
- an insight summary
- a final memo, report, or recommendation

## Companion References

- `references/PHASES_AND_GATES.md`
- `references/TRADING_AND_PIPELINE_USAGE.md`
