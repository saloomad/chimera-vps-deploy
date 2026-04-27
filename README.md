# Chimera VPS Deploy

Deployment configs and operational scripts for the **Kimi Claw VPS** (Alibaba Cloud) running OpenClaw with Kimi K2.6.

## What's Here

| Directory | Purpose |
|-----------|---------|
| `systemd/` | systemd service for openclaw-gateway |
| `cron/` | Trading pipeline cron jobs |
| `scripts/` | Operational scripts (DNS fix, watchdog, sync) |
| `env/` | Environment variable templates |

## Quick Start

```bash
# 1. Clone this repo on the VPS
cd /root
git clone https://github.com/saloomad/chimera-vps-deploy.git chimera-deploy

# 2. Install systemd service
ln -sf /root/chimera-deploy/systemd/openclaw-gateway.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable openclaw-gateway
systemctl start openclaw-gateway

# 3. Install cron jobs
crontab /root/chimera-deploy/cron/trading-pipeline.crontab

# 4. Set up environment
cp /root/chimera-deploy/env/.chimera.env.template /root/.chimera.env
# Edit and fill in API keys
chmod 600 /root/.chimera.env

# 5. Sync trading scripts from main repo
bash /root/chimera-deploy/scripts/sync-from-main-repo.sh
```

## Services

### openclaw-gateway
- Auto-restarts on crash
- Auto-fixes DNS before starting (Alibaba Cloud DNS bug)
- Depends on tailscaled

### Trading Pipeline Cron
- Market scanner: every 30 min
- Candle analyzer: every 30 min
- Bitget derivatives: every 30 min
- Economic calendar: every 6 hours
- Night pipeline: daily 2 AM
- Gateway health check: every 10 min

## Troubleshooting

| Problem | Fix |
|---------|-----|
| DNS failure | `bash /root/chimera-deploy/scripts/fix-dns.sh` |
| Gateway offline | `systemctl restart openclaw-gateway` |
| Discord bot not responding | Check `journalctl -u openclaw-gateway -f` |

## Related Repos

- **Main repo:** [saloomad/chimera](https://github.com/saloomad/chimera) — agents, skills, scripts
- **Connection guide:** See `skills/kimi-vps/SKILL.md` in main repo
