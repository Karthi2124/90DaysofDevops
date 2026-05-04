# Task 1: Your First Dockerfile
# Base image: official Ubuntu
FROM ubuntu:22.04

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install curl using RUN instruction
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Default command: print a message when the container runs
CMD ["echo", "Hello from my custom image!"]