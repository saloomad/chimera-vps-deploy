# Chimera Entry Watch Packet Template

Purpose:

- bridge the gap between a deep bundle and a real trigger
- make wait states explicit instead of vague
- tell `entry-watch` exactly what must happen before the desk upgrades to `READY` or `ACTIVATE`

This document is narrower than the full research bundle.

Use it only after:

- a screener packet selected the symbol
- a research bundle or specialist review established the thesis
- the desk is now waiting for a concrete trigger, reclaim, rejection, sweep, or cooldown reset

## Ownership

Owner:

- `entry-watch`

Supporting contract owners:

- `position-sizer`
- `chart-analyzer`
- `indicator-analyst`

## Entry Watch Packet

```md
# Entry Watch Packet

- entry_watch_packet_id:
- linked_bundle_id:
- linked_screener_packet_id:
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
- owned_by: entry-watch
- observed_at_utc:
- packet_freshness_state:
- wait_state:
- wait_owner:
- trigger_timeframe:
- higher_timeframe_context:
- entry_zone:
- hard_trigger:
- confirmation_needed:
- invalidation_before_entry:
- do_not_chase_rule:
- wake_event:
- wake_sources:
  - item
- chart_confirmation_needed:
- indicator_confirmation_needed:
- derivatives_confirmation_needed:
- alert_plan:
- transition_in_reason:
- why_not_activate_yet:
- strongest_rejected_now_action:
- expires_at_utc:
- on_timeout: stay_watch / downgrade / reset / reject
- next_allowed_states:
  - WATCH
  - READY
  - ACTIVATE
  - RESET
- what_keeps_it_watch_only:
  - item
- what_upgrades_it_to_ready:
  - item
- what_cancels_it:
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

- what exact trigger is still missing
- which timeframe owns the trigger
- what alert or event wakes the desk up
- why the desk stayed in entry-watch instead of activating or rejecting
- what invalidates the idea before entry
- when the wait expires or downgrades
