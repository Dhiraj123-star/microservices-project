from fastapi import FastAPI
import redis
import os

app = FastAPI()

REDIS_HOST = os.getenv("REDIS_HOST","redis-master")
REDIS_PORT=int(os.getenv("REDIS_PORT",6379))

db=redis.Redis(host=REDIS_HOST,port=REDIS_PORT,decode_responses=True)

@app.get("/")
def read_root():
    return {"message":"Gateway Service is running"}

@app.post("/submit-task")
def submit_task(task_name:str):
    db.rpush("tasks",task_name)
    return {"status":"Task submitted","task":task_name}