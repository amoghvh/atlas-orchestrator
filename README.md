# Atlas Distributed Task Orchestrator

Atlas is a high-performance, asynchronous task distribution system built to handle computationally expensive workloads without blocking the primary application flow. It demonstrates a production-grade microservices architecture using **FastAPI**, **Celery**, and **Redis**.

## 🚀 The Architecture
Atlas decouples the request layer from the execution layer:
- **API Layer (FastAPI):** Receives incoming requests and dispatches them instantly.
- **Message Broker (Redis):** Acts as a durable queue for task persistence.
- **Worker Layer (Celery):** A scalable pool of background workers that process tasks horizontally.
- **Observability (Flower):** Real-time monitoring of task health, latency, and success rates.

## 🛠️ Tech Stack
- **Framework:** FastAPI
- **Distributed Tasks:** Celery
- **Message Broker:** Redis
- **Monitoring:** Flower
- **Environment:** Python 3.10+ (WSL/Ubuntu)

## 🚦 Getting Started

### 1. Prerequisite: Start the Broker
Ensure Redis is running on your local machine:
('''bash)

sudo service redis-server start

2. Installation
Bash

git clone [https://github.com/YOUR_USERNAME/atlas-task-distributor.git](https://github.com/YOUR_USERNAME/atlas-task-distributor.git)
cd atlas-task-distributor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Execution (Triple-Terminal Setup)

To run the full distributed system, open three terminal tabs:

Tab 1: The API Control Center
Bash

uvicorn main:app --reload

Tab 2: The Background Workers
Bash

celery -A tasks worker --loglevel=info

Tab 3: Monitoring Dashboard
Bash

celery -A tasks flower --port=5555



Monitoring

Once running, you can monitor the "Atlas" heartbeat and worker performance at:
http://localhost:5555
🎯 Project Goals for 2026

This project was developed as part of a high-value engineering portfolio to demonstrate proficiency in Distributed Systems, Asynchronous Programming, and Infrastructure Scalability during my B.Tech studies at CHRIST (Deemed to be University).


---

