# Day 25 – Reset vs Revert & Branching Strategies

## Git Reset vs Revert

| Feature                   | git reset                     | git revert                           |
| ------------------------- | ----------------------------- | ------------------------------------ |
| What it does              | Moves branch pointer backward | Creates a new commit to undo changes |
| Removes commit history?   | Yes                           | No                                   |
| Safe for shared branches? | No                            | Yes                                  |
| When to use               | Local changes, before pushing | Public/shared branches               |

---

## Reset Types

* **--soft** → keeps changes staged
* **--mixed** → keeps changes unstaged
* **--hard** → deletes everything (dangerous)

### Destructive?

`--hard` is destructive because it permanently deletes changes.

### Should you use reset on pushed commits?

❌ No — it rewrites history and breaks collaboration

---

## Git Revert

* Safely undoes commits
* Keeps history intact
* Best for team environments

---

## Branching Strategies

### 1. GitFlow

**How it works:**
main → production
develop → integration
feature → new features
release → pre-release
hotfix → urgent fixes

**Flow:**
feature → develop → release → main

**Use case:**
Large teams, structured releases

**Pros:**

* Organized
* Stable releases

**Cons:**

* Complex
* Slow

---

### 2. GitHub Flow

**How it works:**
main → always deployable
feature branches → PR → merge

**Flow:**
feature → main

**Use case:**
Startups, fast delivery

**Pros:**

* Simple
* Fast

**Cons:**

* Less control for big teams

---

### 3. Trunk-Based Development

**How it works:**
Everyone works on main (trunk)
Short-lived branches

**Flow:**
small changes → main

**Use case:**
High-speed teams, CI/CD

**Pros:**

* Very fast
* Continuous integration

**Cons:**

* Requires discipline

---

## Answers

### Startup shipping fast?

👉 GitHub Flow

### Large team with releases?

👉 GitFlow

### Open-source projects?

👉 Mostly GitHub Flow or Trunk-Based
