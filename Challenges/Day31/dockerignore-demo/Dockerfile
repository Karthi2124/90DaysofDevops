# Task 5: .dockerignore Demo
# -------------------------------------------------
# The .dockerignore file in this folder excludes:
#   node_modules/  — not copied (too large, reinstall inside)
#   .git/          — not copied (version history unwanted)
#   *.md           — not copied (README.md excluded)
#   .env           — not copied (secrets never go into images!)
#
# To verify what WAS included after building:
#   docker run --rm dockerignore-demo ls -la /app
#   You should only see: app.py
#   node_modules/, .env, README.md, and .git/ will be ABSENT.

FROM python:3.12-slim

WORKDIR /app

# COPY . . sends the build context → Docker daemon
# Files in .dockerignore are excluded before this transfer
COPY . .

CMD ["python", "app.py"]