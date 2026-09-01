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

### `uses`

The `uses` keyword allows me to use an existing GitHub Action.

I used:

```yaml
uses: actions/checkout@v4
```

This checks out my repository code so that the runner can access the files.

### `run`

The `run` keyword is used to execute commands on the GitHub runner.

For example:

```yaml
run: echo "Hello from GitHub Actions!"
```

This prints a message in the GitHub Actions log.

### Branch Name

I used:

```yaml
run: echo "Branch: ${{ github.ref_name }}"
```

GitHub automatically provides the name of the branch.

For example, if I push code to the `main` branch, the output will be:

```text
Branch: main
```

## Simple Workflow Flow

```text
Developer
    ↓
Write or Update Code
    ↓
git add
    ↓
git commit
    ↓
git push
    ↓
GitHub Actions Starts
    ↓
Ubuntu Runner Starts
    ↓
Checkout Code
    ↓
Run Commands
    ↓
Workflow Completed
```

## Successful and Failed Workflow

I learned how to check my workflow in the GitHub Actions tab.

A successful workflow is shown with a green check mark:

```text
🟢 Success
```

A failed workflow is shown with a red cross:

```text
🔴 Failure
```

When a workflow fails, I can open the failed workflow, click the job, and check the error message.

The error message helps me understand what went wrong.

After fixing the problem, I can commit and push the changes again.

GitHub Actions will automatically run the workflow again.

## My Understanding

GitHub Actions helps automate tasks that developers would otherwise need to run manually.

Whenever I push code to GitHub, my workflow can automatically start and execute the steps I define.

I also learned that a pipeline can be successful or fail.

If a pipeline fails, I can read the error logs, fix the problem, and push the changes again.

## What I Learned Today

- How to create a GitHub Actions workflow.
- Where GitHub Actions workflow files are stored.
- How to create a `.yml` file.
- How to trigger a workflow using `push`.
- What `jobs:` means.
- What `runs-on:` means.
- What `steps:` means.
- How to use `uses:`.
- How to use `run:`.
- How to print the branch name.
- How to view GitHub Actions workflow runs.
- How to identify successful and failed workflows.
- How to check workflow error logs.
