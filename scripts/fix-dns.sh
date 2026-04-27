#!/bin/bash
# fix-dns.sh — Fix Alibaba Cloud DNS intermittent failure
# Run as ExecStartPre for openclaw-gateway or manually when DNS breaks

set -e

# Check if systemd-resolved is managing resolv.conf
if systemctl is-active systemd-resolved >/dev/null 2>&1; then
    echo "[fix-dns] Stopping systemd-resolved..."
    systemctl stop systemd-resolved
fi

# Write static resolv.conf with Alibaba DNS
if ! grep -q "223.5.5.5" /etc/resolv.conf 2>/dev/null; then
    echo "[fix-dns] Writing static resolv.conf..."
    cat > /etc/resolv.conf << 'EOF'
nameserver 223.5.5.5
nameserver 223.6.6.6
EOF
    chmod 644 /etc/resolv.conf
fi

# Verify DNS works
if nslookup discord.com >/dev/null 2>&1; then
    echo "[fix-dns] DNS OK"
    exit 0
else
    echo "[fix-dns] DNS still broken, trying Cloudflare..."
    cat > /etc/resolv.conf << 'EOF'
nameserver 1.1.1.1
nameserver 8.8.8.8
EOF
    chmod 644 /etc/resolv.conf
fi

if nslookup discord.com >/dev/null 2>&1; then
    echo "[fix-dns] DNS OK (Cloudflare fallback)"
    exit 0
else
    echo "[fix-dns] CRITICAL: All DNS servers failed"
    exit 1
fi
