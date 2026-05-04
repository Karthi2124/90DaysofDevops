# Task 3: ENTRYPOINT Demo
# -------------------------------------------------
# ENTRYPOINT sets a FIXED executable that always runs.
# Arguments passed at runtime are APPENDED to it, not replacing it.
#
# Usage examples:
#   docker run entrypoint-demo           → runs: echo  (prints empty line)
#   docker run entrypoint-demo hello     → runs: echo hello
#   docker run entrypoint-demo "hi" "there" → runs: echo hi there
#
# Key behavior: runtime args become ARGUMENTS to the entrypoint,
# they do NOT replace it. ENTRYPOINT is the fixed executable.
#
# ENTRYPOINT + CMD together:
#   ENTRYPOINT = the program to run (fixed)
#   CMD        = default arguments (overridable)
#
# Best practice: Use ENTRYPOINT for the main binary,
#                Use CMD for its default flags/args.

FROM alpine:3.19

ENTRYPOINT ["echo"]