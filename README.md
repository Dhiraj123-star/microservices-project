
# 🏗️ Microservices Queue Project

This project demonstrates a decoupled microservices architecture using **FastAPI**, **Redis**, and **Kubernetes**.

## 🚀 Current Features

* **Gateway Service**: A public-facing REST API that accepts tasks.
* **Message Queue**: A Redis instance (StatefulSet) that stores tasks reliably.
* **Asynchronous Flow**: The Gateway receives a request and pushes it to Redis immediately, allowing for high-speed responsiveness.

## 📂 Project Structure

* `gateway-service/`: FastAPI application that produces messages.
* `k8s/`: Kubernetes manifests for Redis and the Gateway.

## 🛠️ How to Interact with the API

### 1. Get the Service URL

To find the entry point of your Gateway, run:

```bash
minikube service gateway-service --url

```

### 2. Submit a Task

Use `curl` to send a task to the queue. Replace `<URL>` with the address from the step above:

```bash
curl "<URL>/submit-task?task_name=MyFirstTask" -X POST

```

**Expected Response:**

```json
{"status": "Task submitted", "task": "MyFirstTask"}

```

## 🔍 Verify Messages in Redis

You can "peek" inside the Redis queue to see your pending tasks using `kubectl`:

```bash
kubectl exec -it redis-master-0 -- redis-cli LRANGE tasks 0 -1

```

---
