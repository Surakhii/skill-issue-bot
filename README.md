# Skill Issue Bot — Dockerized

This repo contains a Discord bot that posts a random "skill issue" GIF in newly created `ticket-...` channels. Below are instructions to build and run it using Docker.

## Prerequisites
- Docker (and optionally Docker Compose)
- Discord bot token and Tenor API key

Required environment variables:
- `DISCORD_TOKEN`: Your Discord bot token
- `TENOR_KEY`: Your Tenor API key

You can place them in a local `.env` file (not committed) like:

```
DISCORD_TOKEN=your_discord_token_here
TENOR_KEY=your_tenor_key_here
```

## Build with Docker

```bash
# From the repo root
docker build -t skill-issue-bot:latest .
```

## Run with Docker

```bash
# Pass env vars directly
docker run --rm \
  -e DISCORD_TOKEN="$DISCORD_TOKEN" \
  -e TENOR_KEY="$TENOR_KEY" \
  --name skill-issue-bot \
  skill-issue-bot:latest
```

Or using an `.env` file:

```bash
docker run --rm --env-file ./.env --name skill-issue-bot skill-issue-bot:latest
```

## Run with Docker Compose

```bash
# Uses docker-compose.yml and loads env from .env
docker compose up --build -d
# To stop
docker compose down
```

## Notes
- The image uses `python:3.11-slim` and installs dependencies from `requirements.txt`.
- `.dockerignore` excludes local caches, venvs, `.env`, and VCS/editor files from the build context.
- The bot expects to run inside a server where it can connect to Discord and Tenor.
