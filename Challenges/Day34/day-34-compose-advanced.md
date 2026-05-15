# Day 34 - Docker Compose Advanced

## Objective

The goal of this task was to build a production-like multi-container application using Docker Compose.

This project includes:

- Node.js Web Application
- PostgreSQL Database
- Redis Cache

The setup demonstrates how multiple services communicate inside Docker Compose using:

- Networks
- Volumes
- Healthchecks
- Restart Policies
- Service Dependencies

---

# Project Structure

```text
day-34/
│
├── docker-compose.yml
├── day-34-compose-advanced.md
│
└── app/
    ├── Dockerfile
    ├── package.json
    └── server.js
```

---

# Application Architecture

```text
 ┌────────────┐
 │ Node.js App│
 │   (Web)    │
 └─────┬──────┘
       │
       │ connects to
       ▼
 ┌────────────┐
 │ PostgreSQL │
 │ Database   │
 └─────┬──────┘
       │
       │ uses cache
       ▼
 ┌────────────┐
 │   Redis    │
 │   Cache    │
 └────────────┘
```

---

# Docker Compose File

## docker-compose.yml

```yaml
version: "3.9"

services:

  web:
    build: ./app

    container_name: node_app

    ports:
      - "5000:5000"

    environment:
      DB_HOST: db
      DB_NAME: mydb
      DB_USER: postgres
      DB_PASSWORD: postgres
      REDIS_HOST: redis

    depends_on:
      db:
        condition: service_healthy

    networks:
      - backend

    labels:
      project: "day34"
      service: "web"

  db:
    image: postgres:15

    container_name: postgres_db

    restart: always

    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres

    volumes:
      - postgres_data:/var/lib/postgresql/data

    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

    networks:
      - backend

    labels:
      project: "day34"
      service: "database"

  redis:
    image: redis:7

    container_name: redis_cache

    restart: unless-stopped

    networks:
      - backend

    labels:
      project: "day34"
      service: "cache"

volumes:
  postgres_data:

networks:
  backend:
```

---

# Node.js Application

## server.js

```javascript
const express = require("express");
const { Client } = require("pg");
const redis = require("redis");

const app = express();

const PORT = 5000;

const dbClient = new Client({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  port: 5432,
});

const redisClient = redis.createClient({
  url: `redis://${process.env.REDIS_HOST}:6379`,
});

app.get("/", async (req, res) => {
  try {

    // PostgreSQL Connection
    await dbClient.connect();

    const dbResult = await dbClient.query("SELECT NOW()");

    // Redis Connection
    await redisClient.connect();

    await redisClient.set("message", "Redis is working!");

    const redisMessage = await redisClient.get("message");

    res.send(`
      <h1>Docker Compose Advanced</h1>

      <h2>PostgreSQL Connected</h2>
      <p>${dbResult.rows[0].now}</p>

      <h2>Redis Connected</h2>
      <p>${redisMessage}</p>
    `);

  } catch (error) {

    console.error(error);

    res.status(500).send("Error connecting services");

  } finally {

    await dbClient.end();

    await redisClient.disconnect();

  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

# package.json

```json
{
  "name": "docker-compose-advanced",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.19.2",
    "pg": "^8.11.5",
    "redis": "^4.6.13"
  }
}
```

---

# Dockerfile

## app/Dockerfile

```dockerfile
FROM node:20

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 5000

CMD ["npm", "start"]
```

---

# Features Implemented

## 1. Multi-Container Architecture

Managed all services using a single `docker-compose.yml` file.

Services:

- Web Application
- PostgreSQL Database
- Redis Cache

---

# 2. depends_on with Healthcheck

Used:

```yaml
depends_on:
  db:
    condition: service_healthy
```

This ensures the Node.js application starts only after PostgreSQL becomes healthy.

---

# 3. PostgreSQL Healthcheck

```yaml
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U postgres"]
  interval: 10s
  timeout: 5s
  retries: 5
```

The healthcheck verifies that PostgreSQL is ready to accept connections.

---

# 4. Restart Policies

Used:

```yaml
restart: always
```

for the PostgreSQL service.

### Observation

When the database container was manually stopped using:

```bash
docker kill postgres_db
```

Docker automatically restarted the container.

---

# Restart Policy Notes

| Restart Policy | Purpose |
|---|---|
| always | Restarts container automatically in all cases |
| on-failure | Restarts only when the container crashes |
| unless-stopped | Restarts unless manually stopped |
| no | No automatic restart |

---

# 5. Custom Dockerfile

Instead of using a prebuilt image for the application, a custom Dockerfile was created.

```yaml
build: ./app
```

This builds the Node.js application directly inside Docker Compose.

---

# 6. Named Volumes

Used named volume:

```yaml
volumes:
  postgres_data:
```

This keeps PostgreSQL data persistent even after container recreation.

---

# 7. Named Networks

Created custom network:

```yaml
networks:
  backend:
```

Benefits:

- Service isolation
- Secure communication
- Easy service discovery

Containers communicate using service names:

- db
- redis

instead of IP addresses.

---

# 8. Scaling Test

Command used:

```bash
docker compose up --scale web=3
```

### Observation

Scaling failed because multiple containers cannot bind to the same host port:

```yaml
ports:
  - "5000:5000"
```

Only one container can bind to port 5000 on the host machine.

---

# Why Scaling Requires Load Balancing

In production environments, scaling usually works together with:

- Nginx
- HAProxy
- Traefik
- Kubernetes Services

These tools distribute traffic between multiple application containers.

---

# Commands Used

## Build and Start Containers

```bash
docker compose up --build
```

---

## Stop Containers

```bash
docker compose down
```

---

## Remove Containers and Volumes

```bash
docker compose down -v
```

---

## View Running Containers

```bash
docker ps
```

---

## View Logs

```bash
docker compose logs
```

---

## Scale Containers

```bash
docker compose up --scale web=3
```

---

# Challenges Faced

## 1. Database Startup Timing

Initially, the application attempted to connect before PostgreSQL was ready.

### Solution

Used:

- healthcheck
- depends_on with condition: service_healthy

---

## 2. Scaling Port Conflict

Scaling the web application caused port conflicts.

### Reason

Multiple containers cannot bind to the same host port.

---

# Outcome

Successfully built a real-world multi-container Docker Compose setup with:

- Node.js
- PostgreSQL
- Redis
- Healthchecks
- Restart Policies
- Named Networks
- Named Volumes
- Service Dependencies
- Scaling Tests

This task provided hands-on experience with production-style Docker Compose architecture.

---

# Learning Summary

Through this project, I learned:

- How Docker Compose manages multiple containers
- How services communicate using networks
- How to use healthchecks effectively
- The importance of restart policies
- Persistent storage using Docker volumes
- Scaling limitations with direct port mapping
- How production systems handle container orchestration

---

# Commands to Run the Project

## Build and Start

```bash
docker compose up --build
```

---

## Open Browser

```text
http://localhost:5000
```

---

## Stop Project

```bash
docker compose down
```

---