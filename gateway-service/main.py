from fastapi import FastAPI
import redis
import os
import time

app = FastAPI()

# Load configuration from environment variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis-master")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

# Initialize Redis client
db = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    password=REDIS_PASSWORD,
    decode_responses=True
)

@app.on_event("startup")
def verify_redis_connection():
    """Verify Redis connection on startup."""
    print(f"Connecting to Redis at {REDIS_HOST}:{REDIS_PORT}...", flush=True)
    try:
        if db.ping():
            print("Successfully connected to Redis with authentication!", flush=True)
    except redis.exceptions.AuthenticationError:
        print("FATAL: Redis Authentication failed. Check REDIS_PASSWORD.", flush=True)
    except Exception as e:
        print(f"Warning: Redis connection failed during startup: {e}", flush=True)

@app.get("/")
def read_root():
    return {"message": "Gateway Service is running"}

@app.post("/submit-task")
def submit_task(task_name: str):
    try:
        db.rpush("tasks", task_name)
        return {"status": "Task submitted", "task": task_name}
    except redis.exceptions.AuthenticationError:
        return {"error": "Internal Server Error: Authentication Failure"}, 500
    except Exception as e:
        return {"error": str(e)}, 500