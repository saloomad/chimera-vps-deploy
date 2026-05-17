# Chimera Thesis Stop Review Template

Purpose:

- review a symbol or setup that looked interesting but was stopped before trade activation
- explain why the desk stayed out
- preserve useful lessons from good rejections, expired waits, or vetoed ideas

Use this document when:

- the screener or bundle looked promising
- the desk did not activate a trade
- the symbol was rejected, vetoed, expired, or downgraded before entry

## Ownership

Primary owners:

- `Deezoh`
- `trade-judge`

Supporting owners:

- `entry-watch`
- `risk-engine`

## Thesis Stop Review Packet

```md
# Thesis Stop Review Packet

- thesis_stop_review_packet_id:
- linked_bundle_id:
- linked_entry_watch_packet_id:
- linked_previous_documents:
  - document_type:
    document_id:
    transition_reason:
- symbol:
- direction:
- review_state: vetoed / expired / downgraded / rejected / no_trade_won
- owned_by:
- observed_at_utc:
- stop_reason_owner:
- stop_reason_summary:
- strongest_stop_evidence:
  - item
- strongest_continue_evidence:
  - item
- why_continue_lost:
- what_would_reopen_the_idea:
  - item
- what_would_keep_it_dead:
  - item
- did_the_stop_prevent_a_bad_trade:
- should_the_symbol_return_to_screener:
- should_it_return_to_bundle:
- should_it_stay_rejected:
- decision_path_review:
  - screener_promotion_verdict:
  - bundle_quality_verdict:
  - entry_watch_timing_verdict:
  - biggest_veto_signal:
  - biggest_missed_continue_signal:
- improvement_queue:
  - instruction_change_candidate:
  - data_source_change_candidate:
  - report_contract_change_candidate:
  - workflow_change_candidate:
  - agent_change_candidate:
- notes_for_future_screening:
```

## Minimum Quality Rules

This packet is not complete unless it says:

- why the desk stayed out
- who or what vetoed continuation
- whether the rejection was good or too conservative
- what would reopen the idea later
- what the desk should repeat or stop repeating for similar non-trade cases
