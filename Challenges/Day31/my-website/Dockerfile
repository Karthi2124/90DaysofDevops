# Task 4: Static Website with Nginx
# -------------------------------------------------
# nginx:alpine is a minimal, production-ready web server image.
# Alpine Linux makes it very lightweight (~25MB total).

FROM nginx:alpine

# Copy our custom HTML page into Nginx's default web root.
# Nginx serves files from /usr/share/nginx/html/ by default.
COPY index.html /usr/share/nginx/html/index.html

# EXPOSE 80 documents that Nginx listens on port 80.
# At runtime, map it with: docker run -p 8080:80 my-website:v1
# Then visit http://localhost:8080 in your browser.
EXPOSE 80

# Nginx's official image already sets the correct CMD to start
# the server in the foreground, so we don't need to override it.
# Default CMD inherited from base image:
#   CMD ["nginx", "-g", "daemon off;"]