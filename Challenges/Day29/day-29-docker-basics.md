# Day 29 – Docker Basics

## 🐳 What is Docker?

Docker is a platform that allows you to package applications and their dependencies into containers so they can run consistently across environments.

---

## 📦 What is a Container?

A container is a lightweight, portable environment that runs applications with all required dependencies.

---

## ⚖️ Containers vs Virtual Machines

| Feature     | Containers     | Virtual Machines |
| ----------- | -------------- | ---------------- |
| Size        | Lightweight    | Heavy            |
| Boot Time   | Seconds        | Minutes          |
| OS          | Shares host OS | Full OS          |
| Performance | Fast           | Slower           |

---

## 🧠 Docker Architecture

* Docker Client → sends commands
* Docker Daemon → executes commands
* Images → blueprint of container
* Containers → running instance
* Registry → stores images (Docker Hub)

---

## 🔄 Architecture Flow

User → Docker CLI → Docker Daemon → Pull Image → Run Container

---

## 🧪 Commands Used

### Run container

```bash
docker run hello-world
```

### Run nginx

```bash
docker run -d -p 8080:80 --name my-nginx nginx
```

### Interactive ubuntu

```bash
docker run -it ubuntu bash
```

### List containers

```bash
docker ps
docker ps -a
```

### Stop & remove

```bash
docker stop my-nginx
docker rm my-nginx
```

### Logs

```bash
docker logs my-nginx
```

### Execute inside container

```bash
docker exec -it my-nginx bash
```

---

## 🔍 Observations

* Containers are fast and lightweight
* Easy to run applications anywhere
* Port mapping exposes container to host
* Detached mode runs in background

---

## 🚀 Key Learning

Docker simplifies application deployment and is essential for modern DevOps workflows.

---
