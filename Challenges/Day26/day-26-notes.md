# Day 26 – GitHub CLI (gh)

##  Authentication

### Login

```bash
gh auth login
```

### Check login status

```bash
gh auth status
```

### Authentication Methods

* Browser (OAuth) login
* Personal Access Token (PAT)
* SSH authentication

---

##  Repository Management

### Create a new repo (with README and clone it)

```bash
gh repo create devops-gh-test --public --clone --add-readme
```

### Clone a repo

```bash
gh repo clone <your-username>/<repo-name>
```

### View repo details

```bash
gh repo view
```

### List all repos

```bash
gh repo list
```

### Open repo in browser

```bash
gh repo view --web
```

### Delete repo (careful)

```bash
gh repo delete devops-gh-test --confirm
```

---

##  Issues

### Create an issue

```bash
gh issue create --title "Bug: Login Issue" --body "Fix login bug" --label bug
```

### List issues

```bash
gh issue list
```

### View issue

```bash
gh issue view 1
```

### Close issue

```bash
gh issue close 1
```

### Use in Automation

* Automatically create issues from scripts
* Track deployment failures
* Generate bug reports

---

##  Pull Requests

### Create branch + commit

```bash
git switch -c feature-gh
echo "GitHub CLI feature" > gh.txt
git add .
git commit -m "Added gh feature"
git push -u origin feature-gh
```

### Create PR

```bash
gh pr create --fill
```

### List PRs

```bash
gh pr list
```

### View PR

```bash
gh pr view 1
```

### Merge PR

```bash
gh pr merge 1 --merge
```

### Merge Methods

* --merge (default)
* --squash
* --rebase

### Review PR

```bash
gh pr checkout 1
gh pr view 1
```

---

##  GitHub Actions (Preview)

### List workflow runs

```bash
gh run list
```

### View workflow run

```bash
gh run view <run-id>
```

### Use in CI/CD

* Monitor pipelines
* Debug failures
* Automate deployments

---

##  Useful gh Commands

### GitHub API

```bash
gh api user
```

### Create a Gist

```bash
gh gist create file.txt
```

### Create a release

```bash
gh release create v1.0
```

### Create alias (shortcut)

```bash
gh alias set co "pr checkout"
```

### Search repos

```bash
gh search repos devops
```

---

## Key Learnings

* GitHub CLI removes need for browser
* Useful for automation and scripting
* Essential for DevOps workflows

---
