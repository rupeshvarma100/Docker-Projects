# Docker Learning Projects

Docker packages apps into lightweight containers that run consistently anywhere - solving "works on my machine" issues.

These 5 hands-on projects teach core Docker skills progressively:

## 📋 Projects

| # | Project | Skill | Status |
|---|---------|-------|--------|
| 1 | Static Nginx Website | Single container |
| 2 | Flask + Redis App | Multi-service Compose |
| 3 | Shared MariaDB + WordPress | Custom networks + Shared DB |
---

## 🚀 Quick Start

# 1. Static Website Hosting with Nginx and Docker
 
This video by Techdox shows you how to host a website using Nginx in Docker. You containerize a web server, add your site files, and run everything in a single container. The tutorial walks through creating a simple Dockerfile (or Docker Compose), setting up Nginx to serve your pages, and starting the container so the site is live. There is no need to install Nginx on your machine because it all runs inside Docker. This keeps the setup clean and reproducible.

# 2. Multi-Container Docker Applications with Docker Compose
 
This video shows how to use Docker Compose to run two services together: a Python Flask backend and a Redis database. All service configurations, including builds, ports, and connections, are defined in one docker-compose.yml file. You start everything with a single command, docker compose up. The containers communicate automatically, and environment settings stay centralized. This makes it easy to run and manage the app on any machine while giving a practical example of handling multiple services in Docker.

# 3. One Database Shared by Multiple Containers
 
In this One Database service for Multiple Docker container Services video, the author shows how to run a single database container and let multiple application containers connect to it. You set up MySQL or another database once in Docker, and each service runs in its own container but connects to the same database through a shared Docker network or proper port mapping. You learn how to configure networking, expose the database port, and link containers for secure communication. This approach helps save resources by centralizing databases and also teaches when a shared database works best versus separate instances.

# 4. Automated Continuous Integration with Jenkins in Docker
 
 # These projects is on how to build a complete continuous integration (CI) pipeline using Jenkins inside Docker to automatically create Docker images when code changes. 
 
   The first Project is to Build & Push React Docker Image with a Jenkins Pipeline, setting up the Jenkins container, creating a pipeline to pull source code, build a Docker image, and optionally run tests or    push the image to a registry. 
   The second project, Automated CI with Jenkins on Docker to Build Docker Images, focuses on a React app, how to connect Jenkins to the source repository, build and tag Docker images, and push them automatically. 
   
Both projects show how containerizing Jenkins keeps your build environment isolated, reproducible, and consistent. Once set up, every code update triggers a fresh build, making deployments reliable and automated.


## 📁 Structure

├── project1/ # Single container

├── project2/ # Multi-service

├── project3/ # One Database Shared by Multiple Containers




**🙏 Thanks to [KDnuggets' 5 Fun Docker Projects](https://www.kdnuggets.com/5-fun-docker-projects-for-absolute-beginners)
**    Thanks to Orihinal content creators and thier video refence mentioned in KDnuggets.com page.

**📹 Disclaimer**:  Original content creators retain full ownership of their videos and materials.
