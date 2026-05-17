# Chimera Active Trade Packet Template

Purpose:

- hold the live or paper management truth once a trade exists
- prevent the desk from managing a live trade out of the original screener packet or static bundle
- keep adds, reductions, trailing, partials, and close logic explicit

Use this document when:

- `desk_state = MANAGE`
- a paper trade or live trade is open
- execution truth now matters more than pre-entry theory

## Ownership

Primary owners:

- `Deezoh`
- `execution`

Supporting owners:

- `position-sizer`
- `risk-engine`
- `trade-judge`

## Active Trade Packet

```md
# Active Trade Packet

- active_trade_packet_id:
- linked_bundle_id:
- linked_entry_watch_packet_id:
- linked_previous_documents:
  - document_type:
    document_id:
    transition_reason:
- linked_next_documents:
  - document_type:
    expected_owner:
    trigger_to_open:
- symbol:
- direction:
- trade_mode: paper / live
- trade_status: pending_fill / partially_filled / filled / managing / closing
- transition_in_reason:
- why_trade_was_opened_now:
- why_not_stay_in_watch:
- opened_at_utc:
- last_updated_at_utc:
- owned_by:
- current_size:
- average_entry:
- stop_state:
- stop_level:
- tp_state:
- tp_levels:
  - item
- break_even_rule_state:
- trailing_rule_state:
- add_rule_state:
- reduce_rule_state:
- current_rr_state:
- book_risk_state:
- same_symbol_exposure_state:
- next_management_question:
- next_management_owner:
- what_would_force_reduction:
  - item
- what_would_force_close:
  - item
- what_would_allow_add:
  - item
- what_would_move_stop:
  - item
- close_trigger_candidates:
  - item
- phase_progression_candidates:
  - next_phase:
    why_it_would_open:
    why_it_is_not_open_yet:
- deezoh_decision_trace:
  - decision_trace_id:
  - decision_owner:
  - decision_question:
  - winning_choice:
  - why_this_choice_won:
  - strongest_rejected_alternative:
  - why_that_alternative_lost:
- notes_for_deezoh:
```

## Minimum Quality Rules

This packet is not complete unless it says:

- whether the trade is actually open
- why the desk opened the trade instead of waiting longer
- what the desk will do next if price moves up, down, or sideways
- what forces a reduction or close
- whether adds are still allowed
- who owns the next management decision
