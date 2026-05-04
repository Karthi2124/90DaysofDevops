# Task 2: Dockerfile with All Key Instructions
# -------------------------------------------------

# FROM — specifies the base image to build upon
FROM ubuntu:22.04

# Prevent interactive prompts during apt installs
ENV DEBIAN_FRONTEND=noninteractive

# RUN — executes a command during the IMAGE BUILD phase
# Each RUN creates a new layer in the image
RUN apt-get update && \
    apt-get install -y bash && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# WORKDIR — sets the working directory inside the container
# All subsequent COPY, RUN, CMD instructions use this as the base path
# If the directory doesn't exist, Docker creates it automatically
WORKDIR /app

# COPY — copies files FROM the host (build context) INTO the image
# Syntax: COPY <host-source> <container-destination>
COPY app.sh ./app.sh

# EXPOSE — documents that the container listens on this port at runtime
# This is metadata only — it does NOT actually publish/open the port
# You still need -p flag when running: docker run -p 8080:8080 ...
EXPOSE 8080

# CMD — sets the default command when a container starts
# Can be overridden at runtime: docker run <image> <custom-command>
# Only the LAST CMD in a Dockerfile takes effect
CMD ["bash", "app.sh"]