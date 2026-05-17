---
name: deezoh-diary-and-trading-journal
description: Use this when Deezoh needs a normal diary, trading journal, missed-trade review, agent-quality review, or automatic learning feedback from trade/process outcomes.
---

# Deezoh Diary And Trading Journal

Use this skill when the task involves:

- Deezoh's normal diary
- actual trade journal
- missed trades
- bad agent analysis
- lessons and patterns
- pre-trade vs post-trade review
- automatic improvement feedback

## Read First

1. `CHIMERA_DEEZOH_DIARY_TEMPLATE.md`
2. `CHIMERA_TRADING_JOURNAL_TEMPLATE.md`
3. `CHIMERA_PIPELINE_OBSERVABILITY_TEMPLATE.md`
4. `agents/deezoh/WORKFLOW.md`
5. `scripts/build_deezoh_diary_and_trade_journal.py`
6. `scripts/build_lifecycle_learning_queue.py`
7. `scripts/run_chimera_trade_lifecycle_cycle.sh`

## Runtime Files

Diary:

- `reports/auto/DEEZOH_DIARY.json`
- `reports/auto/DEEZOH_DIARY.md`
- `reports/auto/DEEZOH_DIARY.jsonl`

Trading journal:

- `reports/auto/TRADING_JOURNAL.json`
- `reports/auto/TRADING_JOURNAL.jsonl`

Feedback:

- `reports/auto/DEEZOH_JOURNAL_FEEDBACK.json`
- `reports/auto/LIFECYCLE_LEARNING_QUEUE.json`

## Rule

The diary and trading journal must be automatic.

Every lifecycle cycle should:

1. refresh observability and Deezoh round state
2. build Deezoh diary
3. build trading journal
4. build diary feedback
5. rebuild lifecycle learning queue from that feedback

## What The Diary Captures

- what Deezoh did this round
- what Deezoh learned
- what agents answered well or badly
- what issues appeared
- what patterns or mistakes appeared
- what trades or moves were missed
- what to improve next cycle

## What The Trading Journal Captures

- actual entered/exited paper or live trades
- pre-trade context from bundle and entry-watch
- post-trade closeout review
- result and R:R
- what to repeat
- what to avoid

## Improvement Loop

If the diary finds an issue, route it to:

- `DEEZOH_JOURNAL_FEEDBACK.json`
- then `LIFECYCLE_LEARNING_QUEUE.json`

Then patch the owner:

- agent instruction
- data source order
- script/report contract
- workflow
- packet template

## Smoke Test

Run:

```bash
python scripts/tests/deezoh_diary_and_trade_journal_smoke.py
```

Live:

```bash
python3 /root/openclawtrading/scripts/build_deezoh_diary_and_trade_journal.py --reports-dir /root/openclawtrading/reports/auto
```

## Good Closeout

A good pass leaves:

- current diary JSON and markdown
- append-only diary JSONL
- current trading journal JSON
- append-only trading journal JSONL
- feedback items
- learning queue updated from feedback
