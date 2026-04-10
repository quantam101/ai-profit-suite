# Trade Gate

Trade Gate is the market intelligence and trade-decision project inside AI Profit Suite Pro.

## Initial structure

- `apps/web/` — public web app and dashboard
- `apps/worker/` — Telegram bot, schedulers, scanners, alerts
- `docs/` — architecture, schema, deployment, ops
- `.env.example` — starter environment variables
- `docker-compose.yml` — local reproducible stack

## Core stack

- GitHub — source of truth
- Supabase — auth, Postgres, storage
- Vercel — web frontend
- Always-on worker runtime — Telegram bot and scheduled scans
- PostHog — analytics
- Sentry — error monitoring
- Cloudflare — perimeter security

## First implementation targets

1. Telegram bot worker
2. Database logging
3. Scheduled scans
4. Saved top picks
5. Web dashboard
