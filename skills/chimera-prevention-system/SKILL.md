---
name: chimera-prevention-system
description: Explain and maintain the Chimera prevention system for Codex CLI and OpenCowork. Use when diagnosing config corruption, socket errors, zombie processes, prevention scripts, broken Codex login, or OpenCowork startup failures.
---

# Chimera Prevention System

> **READ THIS FIRST** before modifying any prevention script or diagnosing a Codex/OpenCowork failure. This skill covers what was built, why, and what can still go wrong.

## What Was Built

Three PowerShell scripts in `C:\Users\becke\scripts\preventive\`:

| Script | Purpose | How Often |
|--------|---------|-----------|
| `codex-config-guard.ps1` | Validates `~/.codex/config.toml` for duplicate keys, conflicting sandbox settings, invalid TOML | Every 5 min |
| `codex-safe-login.ps1` | Wraps `codex login` — detects WinNat port exclusions and auto-uses `--device-auth` if needed | On demand |
| `opencowork-watchdog.ps1` | Kills zombie OpenCowork processes (running but no window) and auto-restarts | Every 1 min |

Auto-start via `run-prevention-loop.ps1` → shortcut in Windows Startup folder.

---

## Root Causes This Fixes

### 1. Config.toml "duplicate key" error
**Why it happens:** TOML doesn't allow mixing `[[array]]` and `[table]` syntax for the same root key. Codex config had both `[[mcp_servers]]` and `[mcp_servers.notion]`.
**Guard fix:** Regex-scans for this pattern, converts `[[mcp_servers]]` entries to `[mcp_servers.name]`, removes conflicting `[windows] sandbox` sections.

### 2. Codex login socket error 10013
**Why it happens:** Windows NAT (WinNat) reserves dynamic TCP port ranges. Codex's OAuth callback server tries to bind a blocked port.
**Wrapper fix:** Queries `netsh int ipv4 show excludedportrange` before login. If any exclusion overlaps 3000-9000, uses `--device-auth` (no local server).

### 3. OpenCowork won't start / window doesn't appear
**Why it happens:** Electron multi-process architecture — renderer crashes, main process stays alive but invisible.
**Watchdog fix:** Checks `MainWindowHandle`. If processes exist but handle = 0, kills all and restarts.

---

## Known Risks & Limitations (READ THIS)

### CRITICAL: PowerShell Execution Policy
The prevention scripts require `ExecutionPolicy Bypass` or `RemoteSigned`. If Windows resets this (updates, Group Policy), scripts silently fail.
**Check:** `Get-ExecutionPolicy`
**Fix:** `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### CRITICAL: Watchdog Can Kill Legitimate Minimized Windows
OpenCowork might minimize to system tray with `MainWindowHandle = 0`. The watchdog will kill it.
**Mitigation:** The watchdog only triggers when `MainWindowHandle = 0` for ALL processes. If even one has a handle, it passes. But if you minimize to tray and the window handle drops to 0 — it gets killed.
**Workaround:** Add a tray-detection check before killing (see TODO below).

### RACE CONDITION: Guard vs Codex Self-Modification
Codex may rewrite `config.toml` internally (e.g., when enabling plugins). If the guard runs mid-write, it could read a half-written file and "fix" it incorrectly.
**Mitigation:** Guard only fixes specific known patterns. It doesn't do a full TOML parse.
**Risk level:** LOW — Codex writes are atomic (temp file + rename).

### FALSE NEGATIVE: Regex TOML Parsing
The guard uses regex, not a real TOML parser. Complex nested structures or quoted keys could be missed.
**Mitigation:** Catches the 3 known failure modes. For unknown corruption, logs "TOML validation failed" but may not auto-fix.

### LOG ROTATION MISSING
`config-guard.log`, `safe-login.log`, and `watchdog.log` grow unbounded. No rotation.
**Mitigation:** Logs are small (text). Check size monthly. Add rotation if any log exceeds 10MB.

### STARTUP SHORTCUT DEPENDS ON USER LOGIN
The `Chimera-Prevention.lnk` in Startup folder only runs when you log in. If the machine reboots and sits at login screen, prevention doesn't run.
**Mitigation:** Use Task Scheduler (requires Admin) for system-level startup: `.\register-prevention-tasks.ps1`

### MEMORY LEAK IN PREVENTION LOOP
`run-prevention-loop.ps1` uses `Start-Job` for background loops. PowerShell jobs leak memory over days.
**Mitigation:** Restart loop weekly, or use `Start-Process` with separate windows instead of jobs.

### SAFE LOGIN DOESN'T HANDLE CODEX PORT CHANGES
The wrapper assumes Codex uses ports 3000-9000 for OAuth callback. If Codex changes this range, the check becomes invalid.
**Mitigation:** The wrapper errs on the side of caution — if it can't read exclusions, it assumes blocked and uses `--device-auth`.

### WINNAT STOP/START (OPTION B) IS DESTRUCTIVE
Stopping WinNat to free ports breaks WSL, Docker, and Hyper-V networking temporarily.
**Recommendation:** Always prefer `--device-auth` over stopping WinNat.

---

## File Locations

| File | Path |
|------|------|
| Prevention scripts | `C:\Users\becke\scripts\preventive\` |
| Config backups | `C:\Users\becke\.codex\config-backups\` |
| Guard log | `C:\Users\becke\.codex\config-guard.log` |
| Safe login log | `C:\Users\becke\.codex\safe-login.log` |
| Watchdog log | `C:\Users\becke\.opencowork\watchdog.log` |
| Startup shortcut | `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Chimera-Prevention.lnk` |

---

## Quick Commands

```powershell
# Check if prevention loop is running
Get-Job -Name "ConfigGuard","OpenCoworkWatchdog"

# Run guard manually
.\codex-config-guard.ps1

# Safe login
.\codex-safe-login.ps1

# Force device auth
.\codex-safe-login.ps1 -ForceDeviceAuth

# Check OpenCowork status
.\opencowork-watchdog.ps1

# View logs
tail ~/.codex/config-guard.log
tail ~/.opencowork/watchdog.log
```

---

## What To Do When Prevention Fails

1. **Config still corrupts:** Check `config-guard.log` — did the guard run? Was there a parse error? Run guard manually to see output.
2. **Login still fails with 10013:** Run `.\codex-safe-login.ps1 -ForceDeviceAuth` to bypass OAuth entirely.
3. **OpenCowork still won't start:** Check `watchdog.log` — is it detecting ghosts correctly? Look for `MainWindowHandle` errors. Kill all processes manually: `taskkill /F /IM "Open Cowork.exe"` then restart.
4. **Prevention loop not running:** Check if shortcut exists in Startup folder. Start manually: `.\run-prevention-loop.ps1`

---

## TODOs / Improvements

- [ ] Add log rotation (10MB cap)
- [ ] Add tray-icon detection to watchdog (avoid killing minimized-to-tray)
- [ ] Replace `Start-Job` with persistent scheduled tasks to avoid memory leak
- [ ] Add email/Discord alert when guard detects corruption
- [ ] Integrate with `FRUSTRATION_LOG.md` for unified error tracking

---

*chimera-prevention-system v1.0 | 2026-05-02 | Source of truth: C:\Users\becke\scripts\preventive\README.md*


## Platform Notes

_Optimized for Codex CLI (automation). For Windows Claude Code interactive, see the canonical version in ~/.codex/skills/.
