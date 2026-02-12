@'
# dockerized-app

Minimal Dockerized Flask app with Postgres + Redis using Docker Compose.

## What is this?
Small Flask API:
- `GET /` — hello
- `GET /health` — checks Postgres + Redis connectivity
- `GET /live` — lightweight liveness endpoint (used for container healthcheck)

## Tech
- Python (Flask)
- Postgres
- Redis
- Docker + Docker Compose

## Run (3 commands)
```bash
cp .env.example .env
docker compose up --build -d
Invoke-WebRequest http://localhost:8000/health -UseBasicParsing | Select-Object -Expand Content

