# Plan And State Template

Use this as the minimum `plan.md` contract before fan-out.

```md
# Plan: [Title]

## Objective
[One sentence describing the real output.]

## User Intent Classification
- Research required: YES or NO
- Writing required: YES or NO
- Code/building required: YES or NO
- Orchestration class: `deep research swarm`
- Expected deliverable: [memo, report, thesis, postmortem, comparison]

## Current Reality
- Date checked: [YYYY-MM-DD]
- Freshness window: [same day, last 7 days, historical point-in-time]
- Known tensions:
  - [tension 1]
  - [tension 2]

## Stage 1 - Landscape Scan
- Owner: `swarm-orchestrator`
- Output: `research/landscape_brief.md`
- Gate: narratives, actors, conflicts, and gaps are explicit

## Stage 2 - Dimension Decomposition
- Owner: `swarm-orchestrator`
- Output: dimension list below
- Gate: dimensions are distinct and still overlap

## Dimensions
1. [Dimension name] - [angle] - owner [worker role or worker id]
2. [Dimension name] - [angle] - owner [worker role or worker id]
3. [...]

## Stage 3 - Parallel Deep Dive
- Owner: `dimension-researcher`
- Output: `research/dim01.md` through `research/dimNN.md`
- Gate: all required files exist and meet the minimum quality bar

## Stage 4 - Cross-Verification
- Owner: `cross-verifier`
- Output: `research/cross_verification.md`
- Gate: every important finding is classified, and conflicts are explicit

## Stage 5 - Targeted Validation
- Owner: `targeted-validator`
- Trigger: only if conflict zone or weak evidence matters
- Output: `research/targeted_validation.md`
- Gate: unresolved conflict is either resolved or preserved honestly

## Stage 6 - Insight Extraction
- Owner: `insight-synthesizer`
- Output: `research/insights.md`
- Gate: at least the key patterns, tensions, and what-remains-unproven are explicit

## Stage 7 - Writing Pipeline
- Owner: `chapter-writer` and `assembly-editor`
- Outputs:
  - `writing/outline.md`
  - `writing/chapter01.md` through `writing/chapterNN.md`
  - `final/report.md`
  - optional export such as `final/report.docx`

## Done Criteria
- all required research artifacts exist
- cross-verification is complete
- conflicts are not hidden
- final output matches the real user ask

## Stop Condition
- `complete` when deliverables and gates pass
- `blocked` when a hard data or approval boundary prevents safe completion
- `iterate` when only specific failed slices need rerun
```

## Per-Worker Prompt Contract

Every worker prompt should contain:

1. mission
2. context from upstream files
3. exact output file path
4. required angles or checks
5. explicit statement to write partial output if blocked
