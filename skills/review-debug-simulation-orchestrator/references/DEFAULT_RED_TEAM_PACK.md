# Default Red-Team Pack

Use this pack by default unless the target clearly needs a different adversarial set.

## Required Cases

1. `stale_but_present_input`
   - a source exists and looks usable, but freshness should have downgraded confidence

2. `contradictory_outputs`
   - two owners or reports disagree and the workflow must decide which one wins

3. `illegal_phase_jump`
   - the system tries to jump to a stronger action without enough proof

4. `no_trade_should_win`
   - one narrow lane looks actionable, but the correct answer is restraint

5. `wrong_symbol_or_side_promotion`
   - routing or scoring pushes the wrong focus symbol or wrong direction

## Output Requirement

For each case, say:

- what input was adversarial
- what should have happened
- what actually happened
- whether the failure was:
  - data quality
  - workflow logic
  - reasoning quality
  - ownership conflict
  - scoring or evaluation drift
