# Shell Scripting: Error Handling

## Overview
This repository contains a collection of shell scripts that demonstrate **error handling techniques** in shell scripting. The goal is to make scripts more **robust**, **reliable**, and **user-friendly** by handling potential errors gracefully.

## Why Error Handling?

In shell scripting, unexpected errors can cause scripts to fail or behave unpredictably. Proper error handling helps:

- **Detect and manage failures** early
- **Prevent crashes** and unexpected behavior
- **Provide meaningful feedback** for easier debugging
- Make automation more **reliable and stable**

## What You Will Learn

- Checking command exit statuses using `$?`
- Using `if` statements for error checking
- Using `trap` for automatic cleanup
- Redirecting error messages to log files
- Creating custom error messages for better clarity

## Tasks Included

### Task 1: Checking Exit Status
- Create a directory and check if the operation was successful using the exit status (`$?`).
- Print a meaningful error message if the command fails.

### Task 2: Using `if` Statements for Error Checking
- Extend the script by adding additional steps (like file creation) and use `if` statements to handle potential errors at each stage.

### Task 3: Using `trap` for Cleanup
- Set up a **trap** to clean up temporary files when the script exits unexpectedly.

### Task 4: Redirecting Errors
- Redirect error messages from failed commands to an `error.log` file instead of cluttering the terminal output.

### Task 5: Creating Custom Error Messages
- Add clear, custom error messages to provide more context and make debugging easier.

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/shell-error-handling.git
    ```
   
2. Navigate to the directory containing the scripts:
    ```bash
    cd shell-error-handling
    ```

3. Run any of the scripts:
    ```bash
    bash task1.sh
    bash task2.sh
    bash task3.sh
    bash task4.sh
    bash task5.sh
    ```

