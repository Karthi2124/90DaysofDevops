# Day 41 – Triggers & Matrix Builds

## Overview

Today I learned different GitHub Actions triggers and matrix builds.

I created workflows for:

- Pull request triggers
- Scheduled triggers
- Manual workflow triggers
- Matrix builds
- Matrix exclude
- Fail-fast behavior

---

# Task 1 – Pull Request Trigger

### File
`.github/workflows/pr-check.yml`

```yaml
name: PR Check

on:
  pull_request:
    branches:
      - main
    types:
      - opened
      - synchronize

jobs:
  pr-check:
    runs-on: ubuntu-latest

    steps:
      - name: PR branch
        run: echo "PR check running for branch: ${{ github.head_ref }}"
```

### What I learned
- `pull_request` runs the workflow when a PR event happens.
- `opened` runs when a PR is created.
- `synchronize` runs when new code is pushed to the PR.
- `github.head_ref` gives the PR branch name.

### Result
PR workflow ran successfully when I opened and updated the PR. ✅

---

# Task 2 – Scheduled Trigger

### File
`.github/workflows/schedule.yml`

```yaml
name: Daily Schedule

on:
  schedule:
    - cron: '0 0 * * *'

jobs:
  scheduled-job:
    runs-on: ubuntu-latest

    steps:
      - name: Scheduled message
        run: echo "Scheduled workflow is running!"
```

### What I learned
- `cron` is used to schedule a workflow.
- `0 0 * * *` means the workflow runs every day at 12:00 AM UTC.
- Monday at 9 AM: `0 9 * * 1` means every Monday at 9 AM UTC.

### Result
Scheduled workflow was created successfully. ✅

---

# Task 3 – Manual Trigger

### File
`.github/workflows/manual.yml`

```yaml
name: Manual Deployment

on:
  workflow_dispatch:
    inputs:
      environment:
        description: "Choose environment"
        required: true
        default: "staging"
        type: choice
        options:
          - staging
          - production

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Show selected environment
        run: |
          echo "Selected environment: ${{ inputs.environment }}"
```

### What I learned
- `workflow_dispatch` allows me to run a workflow manually.
- I created an environment input with:
  - `staging`
  - `production`
- I tested both environments successfully. ✅

---

# Task 4 – Matrix Builds

### File
`.github/workflows/matrix.yml`

I used a matrix to test different Python versions:

```yaml
strategy:
  matrix:
    python-version:
      - "3.10"
      - "3.11"
      - "3.12"
```

This created 3 jobs:
- Python 3.10
- Python 3.11
- Python 3.12

### Multiple Operating Systems

I then added:

```yaml
os:
  - ubuntu-latest
  - windows-latest
```

Now the matrix had:
- 2 operating systems × 3 Python versions = 6 jobs

All 6 jobs ran successfully. ✅

---

# Task 5 – Exclude

I excluded Windows with Python 3.10:

```yaml
exclude:
  - os: windows-latest
    python-version: "3.10"
```

- **Before:** 6 jobs
- **After excluding one combination:** 5 jobs
- **The excluded combination was:** Windows + Python 3.10

---

# Task 6 – Fail-Fast

I added:

```yaml
fail-fast: false
```

Then I intentionally failed one job:

```yaml
- name: Intentional failure
  if: matrix.os == 'windows-latest' && matrix.python-version == '3.11'
  run: exit 1
```

- The Windows + Python 3.11 job failed.
- The other jobs continued running because `fail-fast` was set to `false`.

### What I learned
- `fail-fast: true`: Stops/cancels other matrix jobs when a failure occurs.
- `fail-fast: false`: Allows other matrix jobs to continue even if one job fails.

After testing, I removed the intentional failure and ran the workflow successfully again. ✅

---

# Key GitHub Actions Concepts

| Concept | Meaning |
| :--- | :--- |
| `on:` | Defines when workflow runs |
| `jobs:` | Defines the jobs |
| `runs-on:` | Defines the runner OS |
| `steps:` | Defines the steps in a job |
| `uses:` | Uses an existing GitHub Action |
| `run:` | Runs a shell command |
| `workflow_dispatch:` | Manually runs a workflow |
| `schedule:` | Runs workflow on a schedule |
| `matrix:` | Runs jobs with different combinations |
| `exclude:` | Removes a matrix combination |
| `fail-fast:` | Controls what happens when a matrix job fails |

---

# Final Result

Day 41 completed successfully. ✅

I learned:
- Pull Request triggers
- Scheduled triggers
- Manual triggers
- Workflow inputs
- Matrix builds
- Multiple operating systems
- Matrix exclude
- Fail-fast behavior

### Final Matrix:
- Ubuntu + Python 3.10 ✅
- Ubuntu + Python 3.11 ✅
- Ubuntu + Python 3.12 ✅
- Windows + Python 3.11 ✅
- Windows + Python 3.12 ✅

**Total final jobs:** 5  
**Excluded:** Windows + Python 3.10