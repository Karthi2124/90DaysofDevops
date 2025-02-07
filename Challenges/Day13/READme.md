# Advanced Git & GitHub for DevOps Engineers

Mastering **Git and GitHub** is crucial for **DevOps Engineers** to ensure efficient collaboration, automation, and CI/CD pipeline integration. This guide covers advanced Git techniques and GitHub features used in DevOps workflows.

## 📌 1. Advanced Git Commands

### 🔹 Git Aliases
Speed up workflow with custom shortcuts.
```sh
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.cm "commit -m"
```
Check existing aliases:
```sh
git config --global --list
```

### 🔹 Working with Git Tags
Tags mark specific commits (e.g., releases).
- Create an **annotated tag**:
  ```sh
  git tag -a v1.0 -m "Version 1.0 release"
  ```
- Push tag to remote:
  ```sh
  git push origin v1.0
  ```
- Delete a tag:
  ```sh
  git tag -d v1.0
  git push origin --delete v1.0
  ```

### 🔹 Git Reflog
Recover lost commits or branches.
```sh
git reflog
git reset --hard HEAD@{3}  # Restore an older state
```

### 🔹 Git Interactive Rebase
Clean up commit history.
```sh
git rebase -i HEAD~3  # Modify last 3 commits
```

### 🔹 Git Bisect
Find the commit that introduced a bug.
```sh
git bisect start
git bisect bad HEAD
git bisect good <commit-hash>
```

## 📌 2. GitHub for DevOps

### 🔹 GitHub Actions - CI/CD Pipeline
Automate workflows using **GitHub Actions**.
- Create `.github/workflows/ci.yml`
```yaml
name: CI Pipeline
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 16
      - name: Install Dependencies
        run: npm install
      - name: Run Tests
        run: npm test
```

### 🔹 GitHub Secrets for CI/CD
Store sensitive information securely.
```sh
echo "${{ secrets.AWS_ACCESS_KEY }}"  # Example in GitHub Actions
```

### 🔹 Protecting Branches
Prevent accidental changes.
- Require **pull requests** before merging.
- Require **CI checks** to pass.
- Restrict **force-pushes**.

### 🔹 Managing Releases with GitHub
Automate deployments and release management.
```sh
gh release create v1.0.0 --title "Version 1.0" --notes "Initial release"
```

### 🔹 GitHub CLI for DevOps
Use `gh` CLI for automation.
```sh
gh repo clone username/repo
gh issue create --title "Bug Report" --body "Issue details..."
```

## 📌 3. GitOps and Infrastructure as Code (IaC)
GitOps uses Git as the **source of truth** for infrastructure.
- Use **ArgoCD or Flux** to deploy Kubernetes resources.
- Example **GitOps Workflow**:
  - Developers push code.
  - CI/CD triggers build & tests.
  - CD tool (ArgoCD) pulls manifests from Git.
  - Infrastructure updates automatically.

## 📌 4. Troubleshooting & Debugging

### 🔹 Fixing Merge Conflicts
View conflicts:
```sh
git diff --name-only --diff-filter=U
```
Resolve conflicts, then:
```sh
git add <conflicted-file>
git commit
```

### 🔹 Recovering Deleted Branch
```sh
git reflog
git checkout -b recovered-branch <commit-hash>
```

### 🔹 Debugging CI/CD Failures
- Check logs in GitHub Actions.
- Run CI/CD scripts locally before pushing.
