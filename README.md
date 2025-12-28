# Docker Learning Projects

Docker packages apps into lightweight containers that run consistently anywhere - solving "works on my machine" issues.

These 5 hands-on projects teach core Docker skills progressively:

---

## 📋 Projects

| # | Project | Skill | Access |
|---|---------|-------|--------|
| 1 | Static Nginx Website | Single container | http://localhost |
| 2 | Flask + Redis App | Multi-service Compose | http://localhost:5000 |

---

## 🚀 Quick Start

Project 1
cd project1
docker run --name Rupesh-Website -p 80:80 -v ./content:/usr/share/nginx/html:ro -d nginx:stable-alpine3.23-perl

Project 2
cd project2
docker compose up --build -d

text

---

## 📁 Structure
.
├── project1/ # Single container
├── project2/ # Multi-service
└── README.md

text

## 🛠️ Prerequisites
- Docker & Docker Compose

## 🔍 Check Status
docker ps

text

**Copy-paste ready for your learning repo root README.md**
