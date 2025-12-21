import redis
import os
import time
import sys # Import sys

REDIS_HOST = os.getenv("REDIS_HOST", "redis-master")
REDIS_PORT = int(os.getenv("REDIS_PORT",6379))
db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def process_tasks():
    # Adding flush=True ensures the message hits the console immediately
    print(f"Worker started. Connected to {REDIS_HOST}. Waiting...", flush=True)
    
    while True:
        task = db.blpop("tasks", timeout=0)
        task_name = task[1]
        
        print(f" [🕒] Processing: {task_name}", flush=True)
        time.sleep(5) 
        print(f" [✅] Done: {task_name}", flush=True)

if __name__ == "__main__":
    process_tasks()