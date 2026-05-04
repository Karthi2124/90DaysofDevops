# Task 6: Build Optimization — Layer Caching
# -------------------------------------------------
#
# GOLDEN RULE: Put STABLE things FIRST, FREQUENTLY CHANGING things LAST.
#
# Why? Docker caches each layer. When a layer changes, ALL subsequent
# layers are invalidated and must be rebuilt from scratch.
#
# ❌ BAD ORDER (slow rebuilds):
#   COPY . .                    ← changes every time you edit code
#   RUN pip install -r req.txt  ← cache busted! full reinstall every time
#
# ✅ GOOD ORDER (fast rebuilds):
#   COPY requirements.txt .     ← only changes when deps change
#   RUN pip install -r req.txt  ← cached unless requirements.txt changed
#   COPY . .                    ← app code changes often; copied LAST
#
# To see caching in action:
#   1. Build: docker build -t build-demo:v1 .          (all layers built)
#   2. Edit app.py (change a comment or string)
#   3. Rebuild: docker build -t build-demo:v2 .
#   → Layers 1-5 will say "CACHED" — only the COPY . . step reruns!

FROM python:3.12-slim

# Layer 1: Set working directory (stable — never changes)
WORKDIR /app

# Layer 2: Copy ONLY requirements first (changes rarely)
COPY requirements.txt .

# Layer 3: Install dependencies (expensive — cached unless req.txt changes)
RUN pip install --no-cache-dir -r requirements.txt

# Layer 4: Copy application code LAST (changes frequently)
# Placing this after pip install means dependency cache is preserved
# even when you edit your Python files
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]