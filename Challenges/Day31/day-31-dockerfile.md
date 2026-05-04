# Day 31 – Dockerfile: Build Your Own Images

## 🧾 What I Did in This Project

In this project, I worked on creating and managing Docker images using Dockerfiles.  
I learned how to write Dockerfiles from scratch and build custom images based on different requirements.

First, I created a basic Dockerfile using the Ubuntu image and installed required packages like curl. I built the image and ran a container to verify the output.

Next, I explored all major Dockerfile instructions such as FROM, RUN, COPY, WORKDIR, EXPOSE, and CMD. This helped me understand how Docker builds images step by step using layers.

I then implemented and tested the difference between CMD and ENTRYPOINT by creating separate Dockerfiles and observing how commands behave during runtime.

After that, I built a simple static web application using Nginx. I created an HTML file, copied it into the container, and accessed it through the browser using port mapping.

I also created a `.dockerignore` file to exclude unnecessary files like node_modules, .git, and environment files, which improved build performance and reduced image size.

Finally, I explored Docker build optimization by modifying files and rebuilding images. I observed how Docker uses layer caching and understood why the order of instructions is important for faster builds.

Overall, this project helped me understand how to build, run, and optimize Docker images effectively.