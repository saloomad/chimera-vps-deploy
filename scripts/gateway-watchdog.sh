#!/bin/bash
# gateway-watchdog.sh — Restart OpenClaw gateway if Discord disconnects

LOG=/root/.openclaw/logs/openclaw.log
GATEWAY_PID=$(pgrep -f "openclaw-gateway" || echo "")

# Check if gateway is running
if [ -z "$GATEWAY_PID" ]; then
    echo "[$(date)] Gateway NOT running. Restarting..."
    nohup openclaw-gateway > /dev/null 2>&1 &
    exit 0
fi

# Check last 20 log lines for Discord disconnect
if tail -20 "$LOG" 2>/dev/null | grep -q "disconnected\|fetch failed\|gatewayConnected=false"; then
    DISC_COUNT=$(tail -100 "$LOG" 2>/dev/null | grep -c "disconnected\|fetch failed" || echo "0")
    if [ "$DISC_COUNT" -gt 3 ]; then
        echo "[$(date)] Discord unstable ($DISC_COUNT errors). Restarting gateway..."
        kill "$GATEWAY_PID"
        sleep 3
        nohup openclaw-gateway > /dev/null 2>&1 &
    fi
fi

# Check if gateway process is healthy (not consuming too much CPU)
CPU_USAGE=$(ps -p "$GATEWAY_PID" -o %cpu= 2>/dev/null | tr -d ' ' || echo "0")
if (( $(echo "$CPU_USAGE > 95.0" | bc -l 2>/dev/null || echo "0") )); then
    echo "[$(date)] Gateway CPU spike ($CPU_USAGE%). Restarting..."
    kill "$GATEWAY_PID"
    sleep 3
    nohup openclaw-gateway > /dev/null 2>&1 &
fi
