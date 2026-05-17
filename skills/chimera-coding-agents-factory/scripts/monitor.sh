#!/usr/bin/env bash
SESSION="${1:?Usage: $0 <session_id> [poll_interval]}"
INTERVAL="${2:-60}"
while true; do
    if ! ps -p "$SESSION" > /dev/null 2>&1; then
        echo "[$(date)] Process $SESSION completed"
        break
    fi
    echo "[$(date)] Still running... ($SESSION)"
    sleep "$INTERVAL"
done
