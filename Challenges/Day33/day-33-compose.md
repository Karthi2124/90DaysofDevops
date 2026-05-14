# Day 33 – Docker Compose: Multi-Container Basics

## Objective

The goal of this task was to learn Docker Compose and manage multi-container applications using a single YAML configuration file.

---

# Task 1 – Install & Verify Docker Compose

## Verify Docker Version

```bash
docker --version
```

### Output

```bash
Docker version 29.4.1, build 055a478
```

---

## Verify Docker Compose Version

```bash
docker compose version
```

### Output

```bash
Docker Compose version v5.1.3
```

---

# Task 2 – First Docker Compose File

## Created Folder

```bash
mkdir compose-basics
cd compose-basics
```

---

## docker-compose.yml

```yaml
services:
  nginx:
    image: nginx:latest
    container_name: nginx-compose
    ports:
      - "8080:80"
```

---

## Start Container

```bash
docker compose up -d
```

---

## Verify Running Containers

```bash
docker ps
```

---

## Access Nginx

Opened in browser:

```text
http://localhost:8080
```

Successfully verified the Nginx welcome page.

---

## Stop Container

```bash
docker compose down
```

---

# Task 3 – WordPress + MySQL Multi-Container Setup

## Created Folder

```bash
mkdir wordpress-mysql
cd wordpress-mysql
```

---

## Created `.env`

```env
MYSQL_ROOT_PASSWORD=root123
MYSQL_DATABASE=wordpress
MYSQL_USER=wpuser
MYSQL_PASSWORD=wp123
```

---

## docker-compose.yml

```yaml
services:

  db:
    image: mysql:8.0
    container_name: mysql-db
    restart: always

    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}

    volumes:
      - mysql_data:/var/lib/mysql

  wordpress:
    image: wordpress:latest
    container_name: wordpress-app
    restart: always

    ports:
      - "8082:80"

    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: ${MYSQL_USER}
      WORDPRESS_DB_PASSWORD: ${MYSQL_PASSWORD}
      WORDPRESS_DB_NAME: ${MYSQL_DATABASE}

    depends_on:
      - db

volumes:
  mysql_data:
```

---

# Start WordPress + MySQL

```bash
docker compose up -d
```

---

# Verify Running Containers

```bash
docker ps
```

Verified:

- mysql-db
- wordpress-app

Both containers were running successfully.

---

# Access WordPress

Opened in browser:

```text
http://localhost:8082
```

Successfully completed the WordPress installation setup.

---

# Verify Persistence

Stopped containers:

```bash
docker compose down
```

Started again:

```bash
docker compose up -d
```

Verified that WordPress data still existed after restart.

This confirmed that Docker named volumes were working correctly.

---

# Task 4 – Docker Compose Commands Practiced

## Start in Detached Mode

```bash
docker compose up -d
```

---

## View Running Services

```bash
docker compose ps
```

---

## View Logs

```bash
docker compose logs
```

---

## View Live Logs

```bash
docker compose logs -f
```

---

## View Specific Service Logs

```bash
docker compose logs wordpress
```

```bash
docker compose logs db
```

---

## Stop Services Without Removing

```bash
docker compose stop
```

---

## Restart Services

```bash
docker compose start
```

---

## Remove Containers and Networks

```bash
docker compose down
```

---

## Remove Containers, Networks, and Volumes

```bash
docker compose down -v
```

---

## Rebuild Images

```bash
docker compose up --build
```

---

# Task 5 – Environment Variables

Used environment variables in:

- `.env` file
- `docker-compose.yml`

Verified that Docker Compose successfully picked up variables from the `.env` file.

---

# Key Learnings

- Docker Compose simplifies multi-container management
- Services communicate automatically using service names
- Named volumes provide persistent storage
- Environment variables improve configuration management
- Compose automatically creates networks for services

---

# Project Structure

```text
2026/
└── day-33/
    ├── compose-basics/
    │   └── docker-compose.yml
    │
    ├── wordpress-mysql/
    │   ├── docker-compose.yml
    │   └── .env
    │
    └── day-33-compose.md
```

---

# Git Commands Used

```bash
git add .
git commit -m "Completed Day 33 Docker Compose tasks"
git push origin main
```

---

# Conclusion

Successfully learned and implemented Docker Compose basics by creating:

- Single-container application (Nginx)
- Multi-container application (WordPress + MySQL)

Also practiced:

- Container orchestration
- Networking
- Named volumes
- Environment variables
- Docker Compose commands

```