# Chimera Deezoh Diary Template

This is Deezoh's normal desk diary.

It is not only for trades. It records the full thinking process:

- what Deezoh did this round
- what it looked at
- what it believed
- what it asked agents
- what agents answered badly or well
- what was missed
- what patterns appeared
- what issues should be fixed
- what it learned for next time

## Required Files

Current diary:

- `reports/auto/DEEZOH_DIARY.json`
- `reports/auto/DEEZOH_DIARY.md`

Append-only history:

- `reports/auto/DEEZOH_DIARY.jsonl`

Feedback into learning queue:

- `reports/auto/DEEZOH_JOURNAL_FEEDBACK.json`

## Required Sections

Each diary entry must include:

- `phase`
- `focus_symbol`
- `focus_direction`
- `bias`
- `strategy`
- `what_deezoh_did`
- `what_deezoh_learned`
- `issues_and_patterns`
- `next_improvements`
- `next_cycle_questions`
- `next_best_question`
- `trading_journal_summary`

## What To Capture

Interactions:

- questions asked
- answers received
- which agents answered from fresh reports
- which agents needed direct answers or better output contracts

Analysis:

- current bias
- long vs short vs no-trade
- wait trigger
- what would change the phase

Missed trades:

- confirmed missed moves from strategy diagnostics
- no-trade decisions that later need review
- whether a miss means improve earlier detection or avoid chasing

Issues:

- stale data
- missing reports
- weak agent answers
- vague next question
- phase progression without enough evidence

Learning:

- memory patterns
- must-not-repeat items
- what instruction, source order, or agent contract should improve

## Rule

If a diary entry finds an issue, it must create a feedback item in:

- `DEEZOH_JOURNAL_FEEDBACK.json`

The lifecycle learning queue must consume that feedback on the next cycle.
