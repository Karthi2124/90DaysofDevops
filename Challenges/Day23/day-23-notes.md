# Day 23 – Git Branching & GitHub

## What is a branch in Git?

A branch in Git is a lightweight pointer to a specific commit. It allows you to work on different features or fixes independently without affecting the main codebase.

## Why do we use branches instead of committing everything to main?

Branches help isolate work. This prevents breaking the main code and allows multiple developers to work on different features simultaneously.

## What is HEAD in Git?

HEAD is a pointer that refers to the current active branch or commit you are working on.

## What happens to your files when you switch branches?

When switching branches, Git updates your working directory to match the files from that branch’s latest commit.

---

## origin vs upstream

* origin: Your forked repository (your GitHub repo)
* upstream: Original repository you forked from

---

## git fetch vs git pull

* git fetch: Downloads changes but does NOT merge
* git pull: Downloads AND merges changes automatically

---

## clone vs fork

* clone: Copy of a repo to local machine
* fork: Copy of repo into your GitHub account

## When to use?

* clone → when you just want code locally
* fork → when contributing to someone else's repo

## How to sync fork?

git remote add upstream <original-repo-url>
git fetch upstream
git merge upstream/main
