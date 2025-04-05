# 🐳 Docker Mini Project – Day 18 of 90 Days of DevOps

🗓️ **#Day18 of #90DaysOfDevOps**

Today’s journey took me deeper into the world of **Docker for DevOps Engineers** – focusing on multi-container setups and hands-on container management. 💻⚙️

---

## 🔧 What I Learned:

### 📌 1. Docker Compose Basics
- Created a `docker-compose.yml` file  
- Defined multi-container environments (Flask + MongoDB + Redis)  
- Used `docker-compose up --build` to spin up services  
- Managed inter-service communication (web ↔ database ↔ cache)

### 📌 2. YAML – Human-friendly Configs
- Learned YAML syntax  
- Understood how services, volumes, ports, and environment variables are configured using `.yml`

### 📌 3. Docker Container Management
- 🧰 Pulled an image from **Docker Hub**  
- 👤 Gave non-root user Docker permissions using:
  ```bash
  sudo usermod -aG docker $USER
