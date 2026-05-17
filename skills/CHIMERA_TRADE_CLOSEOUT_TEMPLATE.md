# Chimera Trade Closeout Template

Purpose:

- close the loop after a paper or live trade ends
- document what happened, whether the thesis or management was right, and what should change next time
- stop learning from staying trapped in chat only

Use this document after:

- a trade is closed
- the desk has enough evidence to review the outcome honestly

## Ownership

Primary owners:

- `trade-judge`
- `Deezoh`

Supporting owners:

- `strategy`
- `position-sizer`

## Trade Closeout Packet

```md
# Trade Closeout Packet

- closeout_packet_id:
- linked_bundle_id:
- linked_active_trade_packet_id:
- linked_previous_documents:
  - document_type:
    document_id:
    transition_reason:
- symbol:
- direction:
- trade_mode: paper / live
- opened_at_utc:
- closed_at_utc:
- owned_by:
- close_reason:
- pnl_result:
- rr_result:
- thesis_quality_verdict:
- trigger_quality_verdict:
- management_quality_verdict:
- what_went_right:
  - item
- what_went_wrong:
  - item
- what_was_missed:
  - item
- should_the_same_setup_be_taken_again:
- what_rules_should_change:
  - item
- what_should_be_kept:
  - item
- decision_path_review:
  - screener_promotion_verdict:
  - bundle_promotion_verdict:
  - entry_activation_verdict:
  - management_verdict:
  - which_phase_should_have_stopped_earlier:
  - which_phase_should_have_progressed_earlier:
  - biggest_missed_warning:
  - biggest_missed_confirmation:
- improvement_queue:
  - instruction_change_candidate:
  - data_source_change_candidate:
  - report_contract_change_candidate:
  - workflow_change_candidate:
  - agent_change_candidate:
- learning_capture_status:
- notes_for_future_screening:
```

## Minimum Quality Rules

This packet is not complete unless it says:

- why the trade ended
- whether the thesis was right, late, early, or wrong
- whether management improved or damaged the result
- whether the earlier phase progression decisions were right or wrong
- what the desk should repeat or stop repeating
