# Flask DevOps Application

A Dockerized Flask application with PostgreSQL, ready for production deployment.

## Features

- Docker and Docker Compose support
- PostgreSQL database integration
- Health check endpoint
- Prometheus metrics
- CI/CD pipeline ready

## Getting Started

1. Clone the repository
2. Create `.env` file (see `.env.example`)
3. Run `docker-compose up --build`

## Endpoints

- `GET /` - Main endpoint
- `GET /health` - Health check
- `GET /metrics` - Prometheus metrics