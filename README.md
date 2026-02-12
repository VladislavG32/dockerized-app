[![ci](https://github.com/VladislavG32/dockerized-app/actions/workflows/ci.yml/badge.svg)](https://github.com/VladislavG32/dockerized-app/actions/workflows/ci.yml)

# dockerized-app

Минимальное Dockerized Flask-приложение с Postgres + Redis через Docker Compose.

## Что это
Небольшой API на Flask:
- `GET /` — привет
- `GET /live` — liveness (быстро, без зависимостей)
- `GET /ready` — readiness (Postgres + Redis должны быть доступны)
- `GET /health` — подробная проверка компонентов

## Технологии
- Python (Flask)
- Postgres
- Redis
- Docker + Docker Compose

## Как запустить (3 команды)

### PowerShell (Windows)
```powershell
Copy-Item .env.example .env
docker compose up --build -d
curl.exe http://localhost:8000/health
