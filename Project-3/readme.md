Demonstrates shared database architecture using Portainer stacks—one MariaDB + phpMyAdmin serving multiple app containers (WordPress, Nextcloud, etc.) via custom network.
​

Architecture Overview
text
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   phpMyAdmin    │◄──►│   MariaDB (db)   │◄──►│  WordPress      │
│   localhost:7000│    │   project3-net   │    │  localhost:8081 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              ↑
                       Shared Network + Volumes
Services Breakdown
Service	Image	Purpose	Ports	Volume	Network
db	mariadb:12.2.1-ubi10-rc	Persistent MariaDB database	None (internal)	db:/var/lib/mysql	project3-net
phpmyadmin	phpmyadmin:latest	Web-based DB management	7000:80	None	project3-net
wordpress	wordpress:php8.1-apache	WordPress CMS	8081:80	wordpress:/var/www/html	project3-net (external)
Step-by-Step Deployment
1. Prerequisites
bash
cd "D:\Rupesh Study Material\Docker\Docker-Projects\Project-3"
# Ensure Docker Desktop + WSL/Fedora backend [memory:8]
2. Deploy Database Stack (FIRST)
bash
docker compose -f db.yaml up -d
Creates:

project3-net (user-defined shared network)
​

db volume (persistent /var/lib/mysql)
​

db container (MariaDB 12.2.1 UBI)
​

phpmyadmin (port 7000)
​

Verify: docker compose -f db.yaml ps

3. Setup Database via phpMyAdmin
text
http://localhost:7000
Login: root / password
sql
CREATE DATABASE wordpress CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'admin'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON wordpress.* TO 'admin'@'%';
FLUSH PRIVILEGES;
Note: Leave table name blank during DB creation.
​

4. Deploy WordPress Stack (SECOND)
bash
docker compose -f wordpress.yaml up -d
Joins:

Existing project3-net (external: true)
​

Resolves db hostname via network
​

Creates wordpress volume (/var/www/html)
​

Verify: docker compose -f wordpress.yaml ps

5. Complete WordPress Setup
text
http://localhost:8081 → Follow 5-step wizard
6. Test Connectivity
bash
docker exec -it wordpress ping db              # ✅ Network
docker exec -it wordpress wp db check          # ✅ Database
Key Docker Concepts Explained
Networks: project3-net
text
db.yaml:     networks: project3-net: name: project3-net     # CREATES
wordpress.yaml: networks: project3-net: external: true      # JOINS
User-defined bridge network enables service discovery by container name (db)
​

Prevents stack name prefixing (db_project3-net)
​

Isolates from Project-1/Project-2

Volumes: Persistent Storage
text
db:      name: db              → docker volume inspect db
wordpress: name: wordpress     → docker volume inspect wordpress
Named volumes survive container restarts
​

db:/var/lib/mysql → MariaDB data

wordpress:/var/www/html → WP files/uploads

Container Naming
text
container_name: db          # Clean names (no stack prefix) [attached_file:1]
hostname: db                # DNS resolution on network
Management Commands
bash
# Individual stack control
docker compose -f db.yaml restart
docker compose -f wordpress.yaml down

# Network inspection
docker network inspect project3-net

# Logs
docker compose -f wordpress.yaml logs -f
Scaling Pattern
Add more stacks (Nextcloud, LimeSurvey):

text
# nextcloud.yaml
networks:
  project3-net:
    external: true
    name: project3-net
environment:
  MYSQL_HOST: db  # Same DB!
