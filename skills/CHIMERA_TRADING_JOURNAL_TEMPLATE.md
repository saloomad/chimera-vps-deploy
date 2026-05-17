# Chimera Trading Journal Template

This is the journal for actual trades that were entered and exited.

It is separate from the Deezoh diary because trade review has stricter needs:

- planned entry
- actual entry
- planned stop and targets
- actual exit
- result
- pre-trade reasoning
- post-trade review
- what to repeat
- what to avoid
- what to test next

## Required Files

Current trading journal:

- `reports/auto/TRADING_JOURNAL.json`

Append-only history:

- `reports/auto/TRADING_JOURNAL.jsonl`

Closeout source:

- `reports/auto/TRADE_CLOSEOUT_PACKET_latest.json`

## Required Fields

Each trade row should include:

- `journal_id`
- `symbol`
- `direction`
- `setup_id`
- `entry_price`
- `exit_price`
- `opened_at`
- `closed_at`
- `result`
- `rr_achieved`
- `pre_trade_context`
- `post_trade_review`

## Pre-Trade Review

Judge:

- was the market condition identified correctly?
- did the screener choose the right symbol?
- did the bundle answer the right questions?
- did Deezoh wait for a real trigger?
- did the final decision preserve no-trade when needed?

## Post-Trade Review

Judge:

- was the thesis right?
- was the trigger timely?
- did management help or hurt?
- did the exit follow the plan?
- what should be repeated?
- what should be avoided?
- what should be tested next?

## Learning Rule

Every closed trade should feed:

- `TRADE_CLOSEOUT_PACKET_latest.json`
- `TRADING_JOURNAL.json`
- `DEEZOH_DIARY.json`
- `LIFECYCLE_LEARNING_QUEUE.json`

The trading journal is truth for what happened.
The diary is truth for what Deezoh learned from it.
