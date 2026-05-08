# Checkpoint - 2026-05-05 - Wrong VPS Address Active Defaults Cleanup

## Session Info
- **Ended by**: Codex / Windows
- **Ended at**: 2026-05-05T09:45:00+03:00
- **Platform**: Windows Codex
- **Session focus**: remove stale wrong VPS host/user defaults from active local scripts and shared skill examples

## Original Goal

Stop active files from defaulting to dead VPS addresses or the old `open-claw` user.

## Completed Work
- [x] Verified the fixed Windows SSH helper still reaches `root@100.67.172.114`
- [x] Patched active wrong-host defaults in:
  - `scripts/configure_paperclip_linux_private_auth.sh`
  - `scripts/paperclip_process_worker.py`
  - `scripts/connect_openclaw_linux.ps1`
  - `scripts/open_linux_paperclip_tunnel.ps1`
- [x] Patched bad shared skill SSH examples in:
  - `chimera-vps-deploy/skills/macro-calendar/SKILL.md`
  - `chimera-vps-deploy/skills/news-reader/SKILL.md`
- [x] Removed stale temp patch junk:
  - `.tmp_patch_deezoh.py`
  - `.tmp_patch_inbox.py`
  - `.tmp_patch_macro_bias.py`
  - `.tmp_patch_screener.py`
- [x] Removed stale compiled cache for the old Paperclip worker host list:
  - `scripts/__pycache__/paperclip_process_worker.cpython-313.pyc`
- [x] Re-scanned the touched files and confirmed no remaining:
  - `192.168.1.203`
  - `100.116.214.127`
  - `192.168.31.194`
  - `open-claw@`

## Not Done
- [ ] Broader `/home/open-claw/...` legacy-path cleanup across older scripts, historical notes, and archives is still a separate larger pass

## Files Changed / Created
| File | What Changed |
|------|--------------|
| `scripts/configure_paperclip_linux_private_auth.sh` | switched default Paperclip home to `/root/.paperclip` and default host to `100.67.172.114` |
| `scripts/paperclip_process_worker.py` | switched Linux repo/env defaults to `/root/...`, changed host list to `root@100.67.172.114`, fixed report path map |
| `chimera-vps-deploy/skills/macro-calendar/SKILL.md` | fixed Linux SSH example to `root@100.67.172.114` and `/root/openclawtrading` |
| `chimera-vps-deploy/skills/news-reader/SKILL.md` | fixed Linux SSH example to `root@100.67.172.114` and `/root/openclawtrading` |
| `chimera-vps-deploy/handoffs/CHECKPOINT_2026-05-05_wrong_vps_address_active_defaults_cleanup.md` | this handoff |

## Verification
- `python -m py_compile scripts/paperclip_process_worker.py`
- focused `Select-String` re-scan over all touched files returned no stale wrong-host matches
- `.tmp_patch_*.py` count now returns `0`

## Next Actions
1. If wanted, do a separate bounded pass for active `/home/open-claw/...` runtime-path debt only
2. Ignore historical logs, backups, and archives unless you explicitly want those rewritten too
