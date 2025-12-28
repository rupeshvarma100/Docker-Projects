text
# Static Website Hosting with Nginx and Docker

This repository demonstrates how to host a static website using [Nginx](https://nginx.org/) inside a Docker container.  
You don't need to install Nginx locally — everything runs in a single, reproducible container environment.

---

## 🚀 Features
- Fully containerized Nginx setup  
- Zero local installations required  
- Live static site served through Docker  
- Instant content updates with live reload (no restart required)
- Docker Compose support for advanced workflows

---

## 🧩 Prerequisites
Make sure you have:
- **Docker** and **Docker Compose** installed on your system  
- A directory named `content/` containing your website files (e.g., `index.html`)

---

## 📁 Directory Structure
.
├── content/
│ └── index.html
├── docker-compose.yml (optional)
└── README.md


## 🐳 Option 1: Single Docker Command (Quick Start)

docker run --name Rupesh-Website
-p 80:80
-v ./content:/usr/share/nginx/html:ro
-d nginx:stable-alpine3.23-perl



### Flag Breakdown
| Flag | Description |
|------|--------------|
| `--name Rupesh-Website` | Names your personal website container |
| `-p 80:80` | Maps host port 80 to Nginx port 80 |
| `-v ./content:/usr/share/nginx/html:ro` | Mounts your static files into Nginx (read-only) |
| `-d` | Runs the container in the background |
| `nginx:stable-alpine3.23-perl` | Lightweight, stable Nginx image with Perl support |



## 🐙 Option 2: Docker Compose (Recommended for Multi-file Setups)

Create `docker-compose.yml`:

version: '3.8'
services:
rupesh-website:
image: nginx:stable-alpine3.23-perl
container_name: Rupesh-Website
ports:
- "80:80"
volumes:
- ./content:/usr/share/nginx/html:ro
restart: unless-stopped
environment:
- NGINX_ENTRYPOINT_QUIET_LOGS=1



**Run with Compose:**
docker-compose up -d



**Benefits of Compose:**
- Single command startup
- Auto-restart on crashes
- Easy scaling and configuration
- Environment variables support



## ✅ Verify Container Status
docker ps

OR for Compose:
docker-compose ps

text
See **Rupesh-Website** running on port **80**.



## 🌐 Access Your Website
http://localhost

Your `index.html` served instantly by Nginx!


## ✏️ Live Editing Workflow
cd content/
nano index.html # Edit your page

Refresh browser → INSTANT update (no restart!)


## 📜 Monitor Logs
**Docker command:**
docker logs Rupesh-Website -f


**Docker Compose:**
docker-compose logs -f rupesh-website



## 🧹 Cleanup Commands

**Single Container:**
docker stop Rupesh-Website
docker rm Rupesh-Website



**Docker Compose:**
docker-compose down

With volumes:
docker-compose down -v


## 🔧 Advanced: Custom Nginx Config
Create `nginx.conf` and mount it:
In docker-compose.yml
volumes:

./content:/usr/share/nginx/html:ro

./nginx.conf:/etc/nginx/nginx.conf:ro


**Enjoy your production-ready, Docker-powered Nginx static website! 🚀**
