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

Every worker prompt should include:

1. mission
2. relevant context
3. exact output target

## Required Artifact Shape

Before real fan-out, define the working tree or its logical equivalent:

- `plan.md`
- `research/landscape_brief.md`
- `research/dim01.md` through `research/dimNN.md`
- `research/cross_verification.md`
- `research/targeted_validation.md` when needed
- `research/insights.md`
- `writing/outline.md`
- `writing/chapter01.md` through `writing/chapterNN.md` when writing is parallel
- `final/report.md`
- optional export such as `final/report.docx`

If the platform does not literally use this tree, keep the same logical state contract.

## First Step: Write The Plan

The swarm should not begin with random worker prompts.

Write `plan.md` first.
That plan is the contract for:

- objective
- user intent
- orchestration class
- stage order
- dimensions
- outputs
- gates
- stop condition

Use `references/PLAN_AND_STATE_TEMPLATE.md`.

## Dimension Rules

A dimension is one angle on the same problem.
It is not the same thing as a chapter.

Dimension examples:

- timeframe
- stakeholder
- analytical method
- scenario or tail risk
- sector or sub-market
- flow or data-source angle

Rules:

- each dimension must be meaningfully distinct
- related dimensions should still overlap enough for cross-verification
- each dimension should cover current state, key evidence, and tensions
- use `6-12` dimensions for most serious work
- use `10+` dimensions for full thesis-grade or institutional-grade swarms

## The Seven Phases

### 1. Epistemic Reset And Landscape Scan

The orchestrator should:

- check the current date and freshness horizon
- assume stale internal knowledge until refreshed
- do a coarse-to-fine landscape scan
- identify the dominant narrative, tensions, and open gaps

Output:

- `research/landscape_brief.md`
- initial candidate dimensions inside `plan.md`

### 2. Dimension Decomposition

Break the work into bounded, overlapping dimensions.

Output:

- finalized dimension list in `plan.md`
- optional `research/dimensions.md`

### 3. Parallel Deep Dive

Launch one worker per dimension.

Each worker should:

- gather evidence
- separate stronger findings from weaker findings
- preserve citations or proof references where possible
- write partial output even if incomplete

Cheap worker rule:

- start dimension workers on the cheaper route first
- rerun only failed or ambiguous dimensions on a stronger lane

Output:

- `research/dim01.md` through `research/dimNN.md`

### 4. Cross-Verification

The verifier reads dimension outputs and sorts findings into:

- high confidence
- medium confidence
- low confidence
- conflict zone

Contradictions are signal, not noise.

Output:

- `research/cross_verification.md`

### 5. Targeted Validation

Only run this phase if the conflict zone or weak evidence matters.

Validation should be narrow:

- rerun only the failed dimension
- ask only the unresolved question
- use stronger reasoning only where needed

Output:

- `research/targeted_validation.md`
- or updates folded into `research/cross_verification.md`

### 6. Insight Extraction

The orchestrator or synthesizer should pull out:

- cross-dimensional patterns
- tensions that survived validation
- action-relevant conclusions
- what remains unproven

Output:

- `research/insights.md`

### 7. Writing Pipeline

Writing is separate from research.

The writing phase should:

- preserve evidence and uncertainty
- organize the output for the real user goal
- avoid silently inventing certainty

Output:

- `writing/outline.md`
- `writing/chapterNN.md` when using parallel chapter writers
- `final/report.md`
- optional export artifact such as docx

## Quality Gates

Use pass fail gates between phases.

Minimum gates:

- the landscape is fresh enough to support decomposition
- dimensions are distinct but overlapping
- required dimension outputs exist
- cross-verification records conflict explicitly
- targeted validation resolves or preserves uncertainty honestly
- insights reflect both agreement and unresolved tension
- final writing does not skip the conflict zone

If a gate fails:

- rerun only the failed slice
- do not restart the whole swarm by default

Use `references/PHASES_AND_GATES.md`.

## Sub-Agent Roles

Use these roles explicitly when the platform supports fan-out:

- `swarm-orchestrator`
- `landscape-scanner`
- `dimension-researcher`
- `cross-verifier`
- `targeted-validator`
- `insight-synthesizer`
- `chapter-writer`
- `assembly-editor`
- optional `docx-finisher`

Use `references/SUBAGENT_ROLE_MAP.md`.

## Model Routing

Read `codex-runtime-router` and `model-registry` first when the exact route matters.

Default split:

- orchestrator: strongest planning lane
- verifier: stronger review lane
- final synthesizer: stronger review or planning lane
- dimension workers: cheap execution lane first
- chapter writers: cheap to medium lane depending on stakes

Suggested defaults in this ecosystem:

- architecture analysis and orchestration design: `gpt-5.5` with `high`
- planning and workflow specification: `gpt-5.5` with `high` or `xhigh`
- local skill or document implementation: `gpt-5.4` with `medium`
- cheap workers: `gpt-5.3-codex-spark` with `low` or `gpt-5.4-mini` with `low`
- judgment-heavy review: `gpt-5.5` with `high`
- VPS live execution: `MiniMax-M2.7-highspeed`
- VPS rerun when the first result is weak: `k2.6` with thinking on

## Skill Combination Matrix

This skill is not meant to work alone in a serious workflow.

Typical companions:

- `objective-orchestration-loop`
- `codex-runtime-router`
- `model-registry`
- `openclaw-orchestration-proof-router`
- `pipeline-simulation-lab`
- `strategy-backtest-lab`
- `openclaw-replay-and-backtest`
- `project-operations-manager`
- `agent-session-resume`

Use `references/SKILL_COMBINATION_MATRIX.md`.

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

Use `references/TRADING_AND_PIPELINE_USAGE.md`.

## Challenge And Failure Testing

Before promoting this pattern, pressure-test it against:

- contradictory evidence
- stale data
- weak worker output
- over-decomposition
- wrong-task-type selection
- partial failures and resume paths
- live-pipeline anti-swarm discipline

Use `references/CHALLENGE_SUITE.md`.

## Cheap Worker Verdict Schema

When a cheaper worker is asked for a first-pass orchestration judgment, require a compact verdict schema instead of a loose prose answer.

Minimum fields:

- `orchestration_class`
- `why_not_other_classes`
- `freshness_requirement`
- `required_artifacts`
- `required_gates`
- `stop_condition`
- `rerun_policy`
- `escalation_policy`

This keeps cheap-worker output useful for real orchestration instead of only returning a rough label.

## Expected Deliverables

A good swarm closeout should leave:

- a plan
- a landscape note
- a dimension list
- dimension outputs
- a cross-verification note
- a targeted-validation note when needed
- an insight summary
- a final memo, report, or recommendation

## Companion References

- `references/PLAN_AND_STATE_TEMPLATE.md`
- `references/PHASES_AND_GATES.md`
- `references/SUBAGENT_ROLE_MAP.md`
- `references/SKILL_COMBINATION_MATRIX.md`
- `references/TRADING_AND_PIPELINE_USAGE.md`
- `references/CHALLENGE_SUITE.md`
- `references/WORKER_VERDICT_SCHEMA.md`
