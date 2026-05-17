#!/usr/bin/env bash
# Monitor a background process
# Usage: ./monitor.sh <session_id> [poll_interval] [alert_cmd]

SESSION="${1:?Usage: $0 <session_id> [poll_interval] [alert_cmd]}"
INTERVAL="${2:-60}"
ALERT="${3:-echo 'Process completed'}"

while true; do
    STATUS=$(ps -p "$SESSION" -o state= 2>/dev/null || echo "gone")
    if [ "$STATUS" = "gone" ] || [ -z "$STATUS" ]; then
        echo "[$(date)] Process $SESSION completed"
        eval "$ALERT"
        break
    fi
    echo "[$(date)] Still running... ($SESSION)"
    sleep "$INTERVAL"
done
