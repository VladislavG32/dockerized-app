.PHONY: up down logs ps rebuild tools

up:
docker compose up --build -d

down:
docker compose down -v

logs:
docker compose logs -f --tail=200

ps:
docker compose ps

rebuild:
docker compose up --build -d --force-recreate

tools:
docker compose --profile tools up --build -d
