# Hermes/Windows Path Resolution Workaround

## The Problem

When `learning_feedback_loop.py recall` runs under Hermes (bash subprocess on Windows), it silently fails with:

```
sed: can't read C:\Users\becke\claudecowork\reports\auto\LEARNING_LOOP\RECALL.md: No such file or directory
```

The RECALL.md file was never created. The script returned exit code 0 despite the failure.

## Root Cause

- Hermes spawns a bash (MSYS/git-bash) subprocess on Windows
- bash subprocess cannot resolve raw Windows paths (`C:\Users\...`) — `cd C:\Users\...` fails silently or produces errors
- `cd $HOME` resolves to the MSYS root (`/usr/home/...`), not the Windows user profile
- The script appeared to succeed because the Python subprocess wrapper returned RC 0 — but the actual work happened in the bash child, which failed
- Hermes was reading the (empty) file via Python `open()` — found nothing, reported "clean"

## Symptoms

| Symptom | Cause |
|---------|-------|
| RECALL.md never created despite RC 0 | bash subprocess failed, Python parent reported success |
| `sed: can't read C:\...` in stderr | bash path resolution failure |
| RECALL.md empty but "clean" reported | File existed from prior successful run |

## Diagnostic Pattern

```python
import os, subprocess
base = r"C:\Users\becke\claudecowork"
# Verify path is resolvable via Python first
print(os.path.exists(os.path.join(base, ".learnings", "INBOX.md")))  # Must print True

result = subprocess.run(
    ["python", "scripts/learning_feedback_loop.py", "recall",
     "--output", "reports/auto/LEARNING_LOOP/RECALL.md"],
    cwd=base, capture_output=True, text=True, timeout=60
)
# Check both stdout/stderr AND whether the output file was actually created
output_file = os.path.join(base, "reports", "auto", "LEARNING_LOOP", "RECALL.md")
if result.returncode == 0:
    if os.path.exists(output_file):
        print(f"RECALL.md created OK, size={os.path.getsize(output_file)}")
    else:
        print("WARNING: script returned 0 but RECALL.md was NOT created — bash path failure")
        print("STDERR:", result.stderr)
```

## The Fix in Skill

Session start in `learning-loop` SKILL.md now leads with Python `execute_code` for the recall step, not bash `terminal`. This is the only pattern that works reliably under Hermes cron.

## Prevention Rule

When running any skill from Hermes cron, always:
1. Verify the target paths are resolvable via Python `os.path` before invoking subprocess
2. Check that output files were actually created, not just that the subprocess returned 0
3. Treat bash `cd` to Windows user directories as inherently unreliable in this environment
