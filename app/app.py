import os

from flask import Flask, jsonify
import psycopg2
import redis

app = Flask(__name__)

def check_postgres():
    host = os.getenv("POSTGRES_HOST", "postgres")
    port = int(os.getenv("POSTGRES_PORT", "5432"))
    db = os.getenv("POSTGRES_DB", "appdb")
    user = os.getenv("POSTGRES_USER", "appuser")
    password = os.getenv("POSTGRES_PASSWORD", "apppassword")

    conn = psycopg2.connect(host=host, port=port, dbname=db, user=user, password=password)
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    cur.fetchone()
    cur.close()
    conn.close()
    return True

def check_redis():
    host = os.getenv("REDIS_HOST", "redis")
    port = int(os.getenv("REDIS_PORT", "6379"))
    r = redis.Redis(host=host, port=port, socket_connect_timeout=2, socket_timeout=2)
    return r.ping() is True

@app.get("/")
def hello():
    return "Hello from Dockerized Flask App!\n"

# Liveness: быстрый, без зависимостей
@app.get("/live")
def live():
    return jsonify({"status": "alive"}), 200

# Readiness: зависимости должны быть доступны (DB + Redis)
@app.get("/ready")
def ready():
    try:
        check_postgres()
        check_redis()
        return jsonify({"status": "ready"}), 200
    except Exception as e:
        return jsonify({"status": "not_ready", "error": type(e).__name__}), 503

# Health: подробный статус по компонентам
@app.get("/health")
def health():
    status = {"app": "ok", "postgres": "ok", "redis": "ok"}

    try:
        check_postgres()
    except Exception as e:
        status["postgres"] = f"fail: {type(e).__name__}"

    try:
        check_redis()
    except Exception as e:
        status["redis"] = f"fail: {type(e).__name__}"

    ok = all(v == "ok" for v in status.values())
    return jsonify(status), (200 if ok else 503)

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    app.run(host=host, port=port)
