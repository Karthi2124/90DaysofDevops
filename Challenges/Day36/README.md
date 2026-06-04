# Day 36 - Dockerized Node.js Application

## Overview

This project is a Dockerized Node.js Express API connected to MongoDB.

### Features

* Express REST API
* MongoDB Database
* Dockerized Application
* Docker Compose Setup
* Persistent Database Volume
* Health Checks
* Custom Docker Network

## Run with Docker Compose

```bash
docker compose up -d
```

## Stop Containers

```bash
docker compose down
```

## API Endpoint

```bash
GET /
```

Response:

```json
{
  "message": "Dockerized Node App Running"
}
```

## Environment Variables

```env
PORT=5000
MONGO_URI=mongodb://mongo:27017/dockerdb
```

## Docker Hub Image

```text
docker pull karthikeyanipmec/day36-node-api:v1
```


## Application Chosen

Node.js Express API with MongoDB

## Why I Chose This Project

I wanted a simple but production-like application that demonstrates Docker concepts such as containerization, networking, volumes, health checks, and environment configuration.

---

## Dockerfile Explanation

### Base Image

```dockerfile
FROM node:20-alpine
```

Uses a lightweight Node.js Alpine image.

### Working Directory

```dockerfile
WORKDIR /app
```

Sets the working directory inside the container.

### Copy Dependencies

```dockerfile
COPY app/package*.json ./
```

Copies dependency files.

### Install Dependencies

```dockerfile
RUN npm install --omit=dev
```

Installs only production dependencies.

### Copy Application

```dockerfile
COPY app .
```

Copies application source code.

### Security

```dockerfile
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
```

Runs the application as a non-root user.

### Expose Port

```dockerfile
EXPOSE 5000
```

Makes port 5000 available.

### Start Application

```dockerfile
CMD ["npm", "start"]
```

Starts the Node.js application.

---

## Challenges Faced

1. Docker container name conflict with an existing container named node_app.
2. Removed the old container using:

```bash
docker rm -f node_app
```

3. Re-ran Docker Compose successfully.

---

## Final Result

* Express API running successfully
* MongoDB connected successfully
* Docker Compose orchestration working
* API accessible on localhost:5000

---

## Docker Hub Link

https://hub.docker.com/r/karthikeyanipmec/day36-node-api

---

## Final Image Size

Check using:

```bash
docker images
```
