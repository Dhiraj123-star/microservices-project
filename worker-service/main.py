import redis
import os
import time
import sys

def connect_to_redis():
    # Get values from Environment Variables (injected via ConfigMap and Secret)
    host = os.getenv("REDIS_HOST", "redis-master")
    port = int(os.getenv("REDIS_PORT", 6379))
    password = os.getenv("REDIS_PASSWORD", None)

    while True:
        try:
            print(f"🔄 Attempting to connect to Redis at {host}:{port}...", flush=True)
            r = redis.Redis(
                host=host,
                port=port,
                password=password,
                decode_responses=True,
                socket_connect_timeout=5
            )
            # The ping() command forces the client to authenticate immediately
            if r.ping():
                print(f"✅ Connected to Redis successfully!", flush=True)
                return r
        except redis.exceptions.AuthenticationError:
            print("❌ FATAL: Authentication failed! Check if REDIS_PASSWORD is correct.", flush=True)
            # We sleep longer here because this requires a human fix/config change
            time.sleep(10)
        except Exception as e:
            print(f"⚠️ Connection failed: {e}. Retrying in 5 seconds...", flush=True)
            time.sleep(5)

def process_tasks():
    # Get the authenticated connection
    db = connect_to_redis()
    
    print(f"🚀 Worker started. Waiting for tasks...", flush=True)
    
    while True:
        try:
            # blpop waits for a task to appear in the 'tasks' list
            task = db.blpop("tasks", timeout=0)
            if task:
                task_name = task[1]
                print(f" [🕒] Processing: {task_name}", flush=True)
                time.sleep(5) 
                print(f" [✅] Done: {task_name}", flush=True)
        except Exception as e:
            print(f"⚠️ Lost connection during processing: {e}. Reconnecting...", flush=True)
            db = connect_to_redis()

if __name__ == "__main__":
    process_tasks()