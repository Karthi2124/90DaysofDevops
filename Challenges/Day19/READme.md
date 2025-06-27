# Day19: Multi-Container Apps with Shared Networks and Volumes

This project demonstrates how to build, run, and verify a multi-container application using **Docker Compose**, **shared networks**, and **Docker volumes**.

---

##  Task 1: Building and Running a Multi-Container App with Shared Network and Volumes

Running a multi-container application in Docker typically involves using **separate containers for each service**, such as a web application and a database. This setup follows the best practice of:

> **"One process per container"**

This allows for **independent scaling**, **modular updates**, and easier **service management**.

###  Networking

- By default, Docker containers are **isolated**.
- To enable communication between services (like app ↔ database), place them on the **same Docker network**.
- On the same network, containers can **talk to each other using container names**.

###  Volumes

- **Persistent data** (like database files, images, logs) should **not** be stored inside containers.
- If a container is removed, its filesystem is gone.
- **Docker volumes** provide managed, **persistent storage** that can be shared between containers.

---

##  Task 2: Docker Volumes and File Sharing Verification

Docker volumes are the **preferred method** for persisting and sharing data between containers.

### How Volumes Work:

1. **Create a volume** using:
   ```bash
   docker volume create shared_vol
2. **Mount it in multiple containers** using:

**-v shared_vol:/data**
3. Any data written by one container will be instantly available to others sharing the same volume.
