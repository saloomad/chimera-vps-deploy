# CHECKPOINT - 2026-05-08 GitHub Auto Publish And Bundle Smoke Green

## What changed

- Hardened `github_coordination_guard.py` so Windows Codex can now:
  - auto-refresh and publish shared coordination state
  - auto-publish safe documentation-only updates for the main repo and deploy repo
  - skip safe-doc autopublish when code edits are mixed into the same repo
  - isolate coordination and safe-doc commits with path-scoped `git commit --only -- ...`
- Updated the Windows runner:
  - `scripts/run_windows_codex_github_coordination_sync.ps1`
  - it now runs coordination refresh first, then safe-doc autopublish checks for both repos
- Updated the GitHub coordination workflow docs and skill:
  - `workflows/codex/github-publish-and-shared-sync.md`
  - `skills/github-coordination-gate/SKILL.md`
  - `docs/GITHUB_COORDINATION_OPERATING_GUIDE_2026-05-04.md`
- Fixed the live bundle consumer path:
  - `scripts/tests/current_focus_full_lifecycle_smoke.py`
    - no longer fails on the non-blocking review/debug iterate edge case
  - `scripts/build_bundle_source_proof_matrix.py`
    - `Part 12` now allows stale helpers honestly instead of downgrading the whole section when required strategy evidence is already good

## Live proof

- Windows coordination automation:
  - `github_coordination_guard.py self-test` passed
  - `autopublish-safe-docs` correctly skipped when mixed code edits were present
  - a fresh coordination auto-publish produced an isolated commit touching only:
    - `session-states/windows-codex.yaml`
  - deploy branch parity after that publish:
    - `origin/codex/github-coordination-hardening-part2...HEAD = 0 0`
- VPS bundle/runtime:
  - `CURRENT_FOCUS_FULL_LIFECYCLE_SMOKE.json`
    - `ok = true`
    - `bundle_symbol = BTCUSDT`
    - `review_debug_status = PASS`
  - `RESEARCH_BUNDLE_latest.json`
    - `overall_data_quality = strong`
  - `scripts/tests/research_bundle_contract_smoke.py`
    - `ok = true`
  - `simulate_deezoh_bundle_tail_consumption.py`
    - `OK workflow=range_rotation focus=BTCUSDT posture=no_trade conflicts=3`

## Remaining open work

- Main repo and deploy repo still have broader unrelated dirty work outside this bounded slice.
- The new auto-publisher is safe for coordination and safe documentation-only changes, but it intentionally does not auto-publish mixed code slices.
- If stronger first-class Part 6 chart-board ownership is wanted later, the next improvement is still:
  - direct board owners for `SPX`, `NDX`, and `China` instead of proxy-only support.

## Resume point

If resuming this exact slice:

1. publish the remaining bounded source changes from:
   - `saloomad/chimera`
   - `saloomad/chimera-vps-deploy`
2. keep commit scope isolated because both repos still contain unrelated staged or dirty work
3. if asked to continue Part 6 quality work, move next to stronger direct outside-asset owners rather than more contract rewrites
