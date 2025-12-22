
# 🏗️ Microservices Queue Project

This project demonstrates a decoupled microservices architecture using **FastAPI**, **Redis**, and **Kubernetes**.

## 🚀 Current Features

* **Gateway Service**: A public-facing API that accepts tasks and pushes them to Redis.
* **Message Queue**: A Redis instance (StatefulSet) acting as the message broker.
* **Worker Service**: A background consumer that pulls tasks from Redis and processes them asynchronously.
* **CI/CD Pipeline**: Automated builds via **GitHub Actions** that push images to **Docker Hub** (`dhiraj918106`).
* **Centralized Config**: Uses **Kubernetes ConfigMaps** to manage environment variables (Redis Host/Port) across all services.
* **Real-time Logging**: Unbuffered logging enabled to monitor background tasks instantly.

## 📂 Project Structure

* `.github/workflows/`: CI/CD pipeline definitions.
* `gateway-service/`: FastAPI application (The Producer).
* `worker-service/`: Python background script (The Consumer).
* `k8s/`: Kubernetes manifests for Redis, Gateway, Worker, and ConfigMaps.

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

## ⚙️ Configuration Management

Environment variables are managed via the `redis-config` ConfigMap. To update the Redis host or port cluster-wide:

```bash
kubectl edit configmap redis-config

```

---
