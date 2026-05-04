# Task 3: CMD Demo
# -------------------------------------------------
# CMD sets the DEFAULT command for the container.
# It can be COMPLETELY REPLACED at runtime.
#
# Usage examples:
#   docker run cmd-demo              → prints "hello" (uses CMD default)
#   docker run cmd-demo echo "world" → prints "world" (CMD is replaced)
#   docker run cmd-demo ls /         → lists root dir (CMD is replaced)
#
# Key behavior: the entire CMD is swapped out when you pass arguments.

FROM alpine:3.19

CMD ["echo", "hello"]