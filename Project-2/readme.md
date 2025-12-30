# Multi-Service Flask App with Docker Compose

This repository shows how to use Docker Compose to run two services together: a Python Flask backend and a Redis database.  
All service configurations, including builds, ports, and connections, are defined in one `docker-compose.yml` file.  
You start everything with a single command `docker compose up`. The containers communicate automatically, and environment settings stay centralized.

---

## 🚀 Features
- Multi-container Flask + Redis application  
- Single `docker-compose up` command starts everything  
- Automatic service discovery (Flask ↔ Redis)  
- Centralized configuration management  
- Production-ready service linking

---

## 🧩 Prerequisites
Make sure you have:
- **Docker** and **Docker Compose** installed  
- Python 3.x (for local development)  
- Directory structure with Flask app files

---

## 📁 Directory Structure
.
├── app/

│ ├── app.py # Flask application

│ ├── requirements.txt

│ └── Dockerfile # Flask service build

├── docker-compose.yml # Multi-service configuration

└── README.md


text

---

## 🐳 Flask App Files

### 1. `app/requirements.txt`
Flask==3.0.0
redis==5.0.1

text

### 2. `app/app.py`
from flask import Flask
import redis
import os

app = Flask(name)
redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.route('/')
def hello():
count = redis_client.incr('hits')
return f'Hello from Flask + Redis! I have been seen {count} times.'

if name == "main":
app.run(host='0.0.0.0', port=5000)

text

### 3. `app/Dockerfile`
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

text

---

## 🐙 Docker Compose Configuration

Create `docker-compose.yml`:

version: '3.8'
services:
web:
build: ./app
container_name: flask-web
ports:
- "5000:5000"
depends_on:
- redis
environment:
- FLASK_ENV=production
restart: unless-stopped

redis:
image: redis:alpine
container_name: app-redis
ports:
- "6379:6379"
volumes:
- redis-data:/data
restart: unless-stopped

volumes:
redis-data:

text

---

## 🚀 Start the Application
docker compose up --build -d

text

**What happens:**
- Flask container (`flask-web`) builds and starts on port **5000**
- Redis container (`app-redis`) starts on port **6379**  
- Flask automatically connects to Redis service
- Hit counter persists across restarts!

---

## ✅ Verify Services
docker compose ps

Shows both flask-web and app-redis running
text

**Access your app:**
http://localhost:5000

text
See the hit counter increment with each refresh!

---

## 📜 Monitor Logs
All services:
docker compose logs -f

Specific service:
docker compose logs -f web
docker compose logs -f redis

text

---

## 🧹 Cleanup Commands
Stop services (keeps volumes):
docker compose down

Stop + remove volumes (fresh start):
docker compose down -v

Remove everything including images:
docker compose down -v --rmi all

text

---

## 🔧 Service Communication
**How it works:**
- Flask app uses `redis:6379` (service name as hostname)  
- Docker Compose creates internal DNS automatically
- No hardcoded IPs or ports needed
- Services scale independently

---

## ⚙️ Environment Variables
Add to `docker-compose.yml` under services:
environment:

REDIS_HOST=redis

REDIS_PORT=6379

FLASK_DEBUG=true

text

---

## 🔄 Rebuild & Update
Rebuild after code changes:
docker compose up --build -d

Live reload during development:
docker compose up --build

text

---

**Production-ready Flask + Redis stack running in seconds! 🚀**
