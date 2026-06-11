# Docker Cheat Sheet

## Container Commands

| Command                            | Description                 |
| ---------------------------------- | --------------------------- |
| `docker run image`                 | Run a container             |
| `docker run -it ubuntu bash`       | Run interactively           |
| `docker run -d nginx`              | Run in detached mode        |
| `docker ps`                        | List running containers     |
| `docker ps -a`                     | List all containers         |
| `docker stop <container>`          | Stop a container            |
| `docker start <container>`         | Start a stopped container   |
| `docker restart <container>`       | Restart a container         |
| `docker rm <container>`            | Remove a container          |
| `docker exec -it <container> bash` | Open shell inside container |
| `docker logs <container>`          | View logs                   |
| `docker inspect <container>`       | Detailed container info     |

---

## Image Commands

| Command                                 | Description              |
| --------------------------------------- | ------------------------ |
| `docker images`                         | List images              |
| `docker pull nginx`                     | Download image           |
| `docker build -t myapp:v1 .`            | Build image              |
| `docker tag myapp:v1 username/myapp:v1` | Tag image                |
| `docker push username/myapp:v1`         | Push image to Docker Hub |
| `docker rmi image_id`                   | Remove image             |
| `docker image inspect image_name`       | Inspect image            |

---

## Volume Commands

| Command                                  | Description        |
| ---------------------------------------- | ------------------ |
| `docker volume create data-vol`          | Create volume      |
| `docker volume ls`                       | List volumes       |
| `docker volume inspect data-vol`         | Volume details     |
| `docker volume rm data-vol`              | Remove volume      |
| `docker run -v data-vol:/app/data image` | Mount named volume |

---

## Bind Mounts

| Command                                          | Description           |
| ------------------------------------------------ | --------------------- |
| `docker run -v $(pwd):/app image`                | Mount local directory |
| `docker run -v /host/path:/container/path image` | Bind mount            |

---

## Network Commands

| Command                                  | Description       |
| ---------------------------------------- | ----------------- |
| `docker network create mynet`            | Create network    |
| `docker network ls`                      | List networks     |
| `docker network inspect mynet`           | Inspect network   |
| `docker network connect mynet container` | Connect container |
| `docker network rm mynet`                | Remove network    |

---

## Docker Compose Commands

| Command                  | Description              |
| ------------------------ | ------------------------ |
| `docker compose up`      | Start services           |
| `docker compose up -d`   | Start in background      |
| `docker compose down`    | Stop and remove services |
| `docker compose ps`      | List services            |
| `docker compose logs`    | View logs                |
| `docker compose build`   | Build services           |
| `docker compose restart` | Restart services         |

---

## Cleanup Commands

| Command                  | Description               |
| ------------------------ | ------------------------- |
| `docker system df`       | Docker disk usage         |
| `docker image prune`     | Remove unused images      |
| `docker container prune` | Remove stopped containers |
| `docker volume prune`    | Remove unused volumes     |
| `docker network prune`   | Remove unused networks    |
| `docker system prune -a` | Full cleanup              |

---

## Dockerfile Instructions

### FROM

```dockerfile
FROM node:20-alpine
```

Base image.

### WORKDIR

```dockerfile
WORKDIR /app
```

Set working directory.

### COPY

```dockerfile
COPY . .
```

Copy files.

### RUN

```dockerfile
RUN npm install
```

Execute during build.

### EXPOSE

```dockerfile
EXPOSE 3000
```

Document application port.

### CMD

```dockerfile
CMD ["npm", "start"]
```

Default command.

### ENTRYPOINT

```dockerfile
ENTRYPOINT ["node"]
```

Fixed executable.

---

## CMD vs ENTRYPOINT

| CMD               | ENTRYPOINT                  |
| ----------------- | --------------------------- |
| Easily overridden | Harder to override          |
| Default arguments | Main executable             |
| Flexible          | Consistent startup behavior |

---

## Useful Port Mapping

```bash
docker run -p 8080:80 nginx
```

Host Port → Container Port

8080 (host) → 80 (container)
