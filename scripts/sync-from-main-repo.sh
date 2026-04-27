#!/bin/bash
# sync-from-main-repo.sh — Sync trading scripts from chimera main repo to VPS

set -e

MAIN_REPO="https://github.com/saloomad/chimera.git"
VAPPS_DIR="/root/openclawtrading"
DEPLOY_DIR="/root/chimera-deploy"

# ── Sync main repo ───────────────────────────────────────────────────────────
echo "[sync] Pulling latest from $MAIN_REPO ..."
if [ -d "$VAPPS_DIR/.git" ]; then
    cd "$VAPPS_DIR" && git pull origin main
else
    git clone "$MAIN_REPO" "$VAPPS_DIR"
fi

# ── Ensure scripts are executable ────────────────────────────────────────────
echo "[sync] Setting permissions..."
find "$VAPPS_DIR/scripts" -name "*.py" -exec chmod +x {} \; 2>/dev/null || true
find "$VAPPS_DIR/scripts" -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

# ── Ensure log directory exists ──────────────────────────────────────────────
mkdir -p /root/.openclaw/logs

# ── Restart gateway if config changed ────────────────────────────────────────
if git -C "$VAPPS_DIR" diff --name-only HEAD@{1} HEAD 2>/dev/null | grep -q "openclaw.json"; then
    echo "[sync] openclaw.json changed. Restarting gateway..."
    bash "$DEPLOY_DIR/scripts/gateway-watchdog.sh"
fi

echo "[sync] Done at $(date)"
