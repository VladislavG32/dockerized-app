[![ci](https://github.com/VladislavG32/dockerized-app/actions/workflows/ci.yml/badge.svg)](https://github.com/VladislavG32/dockerized-app/actions/workflows/ci.yml)

# dockerized-app

РњРёРЅРёРјР°Р»СЊРЅРѕРµ Dockerized Flask-РїСЂРёР»РѕР¶РµРЅРёРµ СЃ Postgres + Redis С‡РµСЂРµР· Docker Compose.

## Р§С‚Рѕ СЌС‚Рѕ
РќРµР±РѕР»СЊС€РѕР№ API РЅР° Flask:
- `GET /` вЂ” hello
- `GET /health` вЂ” РїСЂРѕРІРµСЂСЏРµС‚ РґРѕСЃС‚СѓРїРЅРѕСЃС‚СЊ Postgres Рё Redis
- `GET /live` вЂ” Р»С‘РіРєРёР№ liveness endpoint (РёСЃРїРѕР»СЊР·СѓРµС‚СЃСЏ healthcheck РєРѕРЅС‚РµР№РЅРµСЂР°)

## РўРµС…РЅРѕР»РѕРіРёРё
- Python (Flask)
- Postgres
- Redis
- Docker + Docker Compose

## РљР°Рє Р·Р°РїСѓСЃС‚РёС‚СЊ (3 РєРѕРјР°РЅРґС‹)
### PowerShell (Windows)
```powershell
Copy-Item .env.example .env
docker compose up --build -d
curl.exe http://localhost:8000/health

