# Day 35 – Multi-Stage Builds & Docker Hub

## Objective

The goal of this task was to learn:

- How Docker multi-stage builds work
- How to optimize Docker image sizes
- How to push Docker images to Docker Hub
- Docker image best practices
- Image tagging and versioning

---

# Task 1 – Single Stage Docker Build

## Application Used

A simple Node.js Express application.

### server.js

```js
const express = require("express");

const app = express();

app.get("/", (req, res) => {
  res.send("Hello from Multi-Stage Docker Build!");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});