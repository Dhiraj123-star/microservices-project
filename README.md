
# 🏗️ Microservices Queue Project

This project demonstrates a decoupled microservices architecture using **FastAPI**, **Redis**, and **Kubernetes**.

## 🚀 Current Features

* **Gateway Service**: A public-facing API that accepts tasks and pushes them to Redis.
* **Message Queue**: A Redis instance (StatefulSet) acting as the message broker.
* **Worker Service**: A background consumer that pulls tasks from Redis and processes them asynchronously.
* **CI/CD Pipeline**: Automated builds via **GitHub Actions** that push images to **Docker Hub** (`dhiraj918106`).
* **🔐 Secure Authentication**: Full end-to-end security using **Kubernetes Secrets** to manage and inject Redis passwords into all services.
* **🛡️ Infrastructure Hardening**: Redis StatefulSet configured with password-protected access and shell-managed variable expansion for the server entrypoint.
* **🚦 Self-Healing & Readiness**: Integrated **Kubernetes Readiness Probes** for Redis, ensuring that Gateway and Worker services only attempt to connect when the database is authenticated and healthy.
* **🔄 Resilient Connection Logic**: Both Gateway and Worker feature automated retry mechanisms and connection verification (`ping()`) to handle network blips or database restarts without crashing.
* **Centralized Config**: Uses **Kubernetes ConfigMaps** to manage environment variables (Redis Host/Port) across all services.

## 📂 Project Structure

* `.github/workflows/`: CI/CD pipeline definitions.
* `gateway-service/`: FastAPI application (The Producer).
* `worker-service/`: Python background script (The Consumer).
* `k8s/`: Kubernetes manifests for Redis (StatefulSet), Services, Gateway, Worker, ConfigMaps, and **Secrets**.

## 🛠️ How to Interact with the API

### 1. Configure Security

Ensure the Redis Secret is created in the cluster before deployment:

```bash
kubectl create secret generic redis-auth --from-literal=redis-password=<your-password>

```

### 2. Monitor the Worker

Start watching the worker logs to see the authenticated connection and task processing:

```bash
kubectl logs -f -l app=worker

```

### 3. Submit a Task

Get the Gateway URL and send a POST request:

```bash
# Get URL
minikube service gateway-service --url

# Submit Task
curl "<URL>/submit-task?task_name=SecureDataProcess" -X POST

```

**Expected Response:** `{"status": "Task submitted", "task": "SecureDataProcess"}`

## ⚙️ Configuration Management

* **Networking**: Managed via `redis-config` ConfigMap.
* **Security**: Managed via `redis-auth` Secret.
* **Service Discovery**: Uses `redis-master` ClusterIP service for internal communication.

---
