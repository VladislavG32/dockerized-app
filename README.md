# dockerized-app

Минимальное Dockerized Flask-приложение с Postgres + Redis через Docker Compose.

## Что это
Небольшой API на Flask:
- `GET /` — hello
- `GET /health` — проверяет доступность Postgres и Redis
- `GET /live` — лёгкий liveness endpoint (используется healthcheck контейнера)

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
