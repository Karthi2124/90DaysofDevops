# Day 40 – My First GitHub Actions Workflow

## My Learning

Today, I learned how to create and run my first GitHub Actions workflow.

I learned that GitHub Actions can automatically run tasks when I push my code to a GitHub repository.

## What I Did

First, I created a GitHub repository called `github-actions-practice`.

Then, I created the GitHub Actions workflow folder:

```text
.github/workflows/
```

Inside this folder, I created a workflow file called:

```text
hello.yml
```

## My First Workflow

My workflow runs automatically whenever I push code to GitHub.

The workflow performs the following tasks:

- Checks out the repository code.
- Prints a greeting message.
- Prints the current date and time.
- Prints the branch name.
- Lists the repository files.
- Prints the operating system information.

## My Workflow File

The workflow file I created is:

```yaml
name: My First GitHub Actions Workflow

on:
  push:

jobs:
  greet:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Print greeting
        run: echo "Hello from GitHub Actions!"

      - name: Print date and time
        run: date

      - name: Print branch name
        run: echo "Branch: ${{ github.ref_name }}"

      - name: List repository files
        run: ls -la

      - name: Print operating system
        run: uname -a
```

## What I Learned

### GitHub Actions

GitHub Actions is a tool that helps automate tasks in a GitHub repository.

It can automatically run commands for tasks such as testing, building, and deploying applications.

### Workflow

A workflow is a set of instructions that GitHub Actions follows.

My workflow is stored inside:

```text
.github/workflows/hello.yml
```

### Trigger

I used the `push` trigger.

```yaml
on:
  push:
```

This means that whenever I push new code to GitHub, the workflow starts automatically.

```text
git push
    ↓
GitHub Actions starts
```

### Job

A job contains the tasks that GitHub Actions needs to perform.

My workflow has one job called:

```text
greet
```

### Runner

The runner is the machine that executes the workflow.

I used:

```yaml
runs-on: ubuntu-latest
```

This means GitHub runs my workflow on an Ubuntu machine.

### Steps

Steps are the individual tasks inside a job.

My workflow has multiple steps that run one after another.

### `name:` (on a step)

The `name:` key gives each individual step a clear, human-readable title. 

In the GitHub Actions execution UI, this name is displayed next to the step status icon (green check or red cross), making it very easy to track progress and identify which command is running or failing.

### `uses:`

The `uses:` keyword allows me to use an existing pre-built GitHub Action from the GitHub Marketplace or community.

I used:

```yaml
uses: actions/checkout@v4
```

This checks out my repository code onto the runner machine so that subsequent steps can access and work with the files.

### `run:`

The `run:` keyword executes command-line programs and shell scripts directly on the runner.

For example:

```yaml
run: echo "Hello from GitHub Actions!"
```

This runs an `echo` command inside bash on the Ubuntu runner and prints the output directly into the workflow execution logs.

### Branch Name (`${{ github.ref_name }}`)

GitHub Actions provides built-in context variables through the `${{ ... }}` syntax.

I used:

```yaml
run: echo "Branch: ${{ github.ref_name }}"
```

GitHub automatically populates `${{ github.ref_name }}` with the branch or tag name that triggered the run (for example, `main`).

## Simple Workflow Flow

```text
Developer
    ↓
Write or Update Code
    ↓
git add & git commit
    ↓
git push
    ↓
GitHub Actions Triggered (on: push)
    ↓
Ubuntu Runner Provisioned (runs-on: ubuntu-latest)
    ↓
Steps Executed Sequentially:
  1. Checkout code (actions/checkout@v4)
  2. Print greeting (echo)
  3. Print date and time (date)
  4. Print branch name (echo ${{ github.ref_name }})
  5. List repo files (ls -la)
  6. Print OS info (uname -a)
    ↓
Workflow Status: 🟢 Succeeded
```

## Task 5: Testing Pipeline Failure & How to Read Errors

To understand how GitHub Actions handles failures, I tested a deliberate failure:

### 1. What Does a Failed Pipeline Look Like?
- The workflow run is flagged with a distinct **red cross (❌ Failure)** in the Actions tab.
- In the job execution graph, the specific step that threw a non-zero exit code (e.g., `exit 1` or a command not found) turns **red**.
- Any steps scheduled **after** the failed step are automatically skipped, protecting downstream systems from running on a broken state.

### 2. How to Read and Troubleshoot the Error
1. Go to the **Actions** tab of the repository.
2. Click on the failed workflow run (marked in red).
3. Click on the failed job (e.g., `greet`).
4. GitHub Actions automatically expands the step that failed and highlights the terminal error in red.
5. Review the error message and exit code (for example: `Process completed with exit code 1`).
6. Fix the code or configuration locally, commit, and push again. The workflow will re-run automatically.

## Pipeline Run Screenshot

Below is the verified green run of the pipeline:

![First Green Pipeline Run](./first-green-run.png)

## What I Learned Today

- How to create a GitHub Actions workflow inside `.github/workflows/`.
- How YAML syntax powers GitHub Actions configurations.
- The core anatomy: `on:`, `jobs:`, `runs-on:`, `steps:`, `uses:`, `run:`, and `name:`.
- How to access built-in GitHub context variables such as `${{ github.ref_name }}`.
- How to view logs, monitor execution, and analyze both successful (🟢) and failed (🔴) pipelines in the cloud.
