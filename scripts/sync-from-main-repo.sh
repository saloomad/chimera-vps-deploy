#!/bin/bash
# sync-from-main-repo.sh — Sync approved production code into the VPS runtime tree

set -euo pipefail

REPO_URL="https://github.com/saloomad/chimera.git"
BRANCH="production"
RUNTIME_DIR="/root/openclawtrading"
DEPLOY_DIR="/root/chimera-deploy"
TMP_ROOT="$(mktemp -d /tmp/chimera-production-sync.XXXXXX)"
TMP_REPO="$TMP_ROOT/repo"

cleanup() {
    rm -rf "$TMP_ROOT"
}
trap cleanup EXIT

echo "[sync] Preparing approved branch snapshot from $REPO_URL ($BRANCH) ..."

if [ -d "$RUNTIME_DIR/.git" ]; then
    cd "$RUNTIME_DIR"
    PREV_HEAD="$(git rev-parse HEAD)"
    git fetch origin "$BRANCH"
    git checkout "$BRANCH"
    git pull origin "$BRANCH"
    NEW_HEAD="$(git rev-parse HEAD)"

    echo "[sync] Runtime Git checkout updated: $PREV_HEAD -> $NEW_HEAD"
else
    git clone --depth 1 --branch "$BRANCH" "$REPO_URL" "$TMP_REPO"
    SRC_HEAD="$(git -C "$TMP_REPO" rev-parse HEAD)"

    mkdir -p "$RUNTIME_DIR"
    rsync -a --exclude '.git' "$TMP_REPO"/ "$RUNTIME_DIR"/

    echo "[sync] Runtime tree refreshed from approved commit $SRC_HEAD"
fi

echo "[sync] Setting permissions..."
find "$RUNTIME_DIR/scripts" -name "*.py" -exec chmod +x {} \; 2>/dev/null || true
find "$RUNTIME_DIR/scripts" -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true

mkdir -p /root/.openclaw/logs

echo "[sync] Done at $(date)"
