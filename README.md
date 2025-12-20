
# 🏗️ Microservices Queue Project

This project demonstrates a decoupled microservices architecture using **FastAPI**, **Redis**, and **Kubernetes**.

## 🚀 Current Features

* **Gateway Service**: A public-facing API that accepts tasks and pushes them to Redis.
* **Message Queue**: A Redis instance (StatefulSet) acting as the message broker.
* **Worker Service**: A background consumer that pulls tasks from Redis and processes them asynchronously.
* **Real-time Logging**: Unbuffered logging enabled to monitor background tasks instantly.

## 📂 Project Structure

* `gateway-service/`: FastAPI application (The Producer).
* `worker-service/`: Python background script (The Consumer).
* `k8s/`: Kubernetes manifests for Redis, Gateway, and Worker.

## 🛠️ How to Interact with the API

### 1. Monitor the Worker

Before sending tasks, start watching the worker logs in your terminal:

```bash
kubectl logs -f -l app=worker

```

### 2. Submit a Task

In a new terminal, get the Gateway URL and send a POST request:

```bash
# Get URL
minikube service gateway-service --url

# Submit Task
curl "<URL>/submit-task?task_name=SendWelcomeEmail" -X POST

```

**Expected Response:** `{"status": "Task submitted", "task": "SendWelcomeEmail"}`

### 3. Verify the Workflow

* **Gateway**: Responds instantly (the user doesn't wait).
* **Worker**: Picks up the task, waits 5 seconds (simulated work), and logs the completion.

## 🔍 Verify Messages in Redis

If the worker is stopped, you can see pending tasks in the "tasks" list:

```bash
kubectl exec -it redis-master-0 -- redis-cli LRANGE tasks 0 -1

```

---