# Day 37 Docker Revision

## Self Assessment Checklist

| Topic                                | Status |
| ------------------------------------ | ------ |
| Run container from Docker Hub        | Can Do |
| List, stop, remove containers/images | Can Do |
| Explain image layers and cache       | Can Do |
| Write Dockerfile                     | Can Do |
| CMD vs ENTRYPOINT                    | Can Do |
| Build and tag image                  | Can Do |
| Named volumes                        | Can Do |
| Bind mounts                          | Can Do |
| Custom networks                      | Can Do |
| Docker Compose                       | Can Do |
| Environment variables                | Can Do |
| Multi-stage builds                   | Shaky  |
| Push image to Docker Hub             | Can Do |
| Healthchecks & depends_on            | Shaky  |

---

# Quick-Fire Questions

## 1. Difference between Image and Container?

An image is a read-only template used to create containers.

A container is a running instance of an image.

---

## 2. What happens to data when a container is removed?

Container filesystem data is deleted unless stored in a volume or bind mount.

---

## 3. How do containers communicate on a custom network?

They communicate using container names as DNS hostnames.

Example:

```bash
ping db
```

---

## 4. Difference between:

```bash
docker compose down
```

and

```bash
docker compose down -v
```

`down` removes containers and networks.

`down -v` additionally removes volumes.

---

## 5. Why are multi-stage builds useful?

* Smaller images
* Better security
* Faster deployments
* Separate build/runtime environments

---

## 6. Difference between COPY and ADD?

### COPY

Copies local files.

```dockerfile
COPY . .
```

### ADD

Can extract archives and download URLs.

```dockerfile
ADD app.tar.gz /app
```

Prefer COPY unless ADD features are required.

---

## 7. What does:

```bash
-p 8080:80
```

mean?

Maps host port 8080 to container port 80.

---

## 8. Check Docker disk usage

```bash
docker system df
```

---

# Weak Areas to Revisit

## Multi-stage Builds

Practice:

```dockerfile
FROM node:20 AS build

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html
```

---

## Healthchecks

Example:

```yaml
services:
  app:
    image: myapp
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000"]
      interval: 30s
      timeout: 5s
      retries: 3
```

---

# Revision Summary

Topics revised:

* Containers
* Images
* Dockerfile
* Volumes
* Bind Mounts
* Networks
* Docker Compose
* Environment Variables
* Multi-stage Builds
* Docker Hub
* Healthchecks

Ready to move to Day 38.
