# From Docker Errors to a Working Flask App: My Debugging Journey 🐳

After hitting multiple roadblocks while containerizing a Flask application with PostgreSQL, I finally got everything working! Here's what I learned:

##  The Problem
- Flask app failing to start in Docker
- Mysterious port conflicts (even when ports appeared free)
- `before_first_request` deprecation in Flask 2.3
- Gunicorn connection issues

## 🔍 The Debugging Process
1️ Verified container networking with `docker port` and `netstat`  
2️ Checked for zombie processes with `docker ps -a` and `docker rm -f`  
3️ Replaced deprecated Flask decorators with modern alternatives  
4️ Tested database connectivity separately  
5️ Used `docker-compose logs -f` to track startup errors  

## 🛠 Key Solutions
 Complete system cleanup with `docker-compose down -v --remove-orphans`  
 Switched from `before_first_request` to `app_context`  
 Verified port mappings through multiple methods  
 Implemented proper health checks and Prometheus metrics  

##  Lessons Learned
🔹 Always check BOTH host AND container port usage  
🔹 Modern Flask versions need updated initialization patterns  
🔹 Docker's caching can sometimes hurt more than help  
🔹 Comprehensive logging saves hours of debugging  

##  Final Architecture
- **Flask 2.3 + Gunicorn**
- **PostgreSQL container**
- **Prometheus monitoring**
- **CI/CD ready configuration**

Big thanks to the Docker community for helping me work through these challenges! The satisfaction of finally seeing that "healthy" status from the health check endpoint was worth all the effort 💪

---

## 🚀 Running the Application

### Prerequisites
- Docker & Docker Compose installed
- PostgreSQL container ready
- `.env` file configured (example provided below)

### Steps to Run
```bash
# Clone the repository
git clone https://github.com/your-repo/docker-flask-app.git
cd docker-flask-app

# Build and start containers
docker-compose up --build
```

### Example `.env` file
```env
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_DB=mydatabase
FLASK_ENV=development
```

### Checking Running Containers
```bash
docker ps
```

### Viewing Logs
```bash
docker-compose logs -f
``
