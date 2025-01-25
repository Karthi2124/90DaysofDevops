# Shell Scripting Challenge 🚀

This repository contains a Bash script that demonstrates fundamental shell scripting concepts through various tasks, including comments, variables, wildcards, and more.

## Tasks Overview

### Task 1: Comments
**Purpose:** Add explanatory notes to the script to describe its functionality.
- Comments in Bash scripts start with `#` and are ignored by the shell during execution.

### Task 2: Echo
**Purpose:** Use the `echo` command to print text or variable values to the terminal.

### Task 3: Variables
**Purpose:** Define and assign values to variables for reuse in the script.

### Task 4: Using Variables
**Purpose:** Retrieve and display the values stored in the variables.

### Task 5: Using Built-in Variables
**Purpose:** Utilize Bash’s built-in variables to get information about the script's execution, such as:
- `$0`: Script name.
- `$#`: Number of arguments passed.
- `$@`: All arguments passed.
- `$PWD`: Current working directory.
- `$HOME`: User's home directory.

### Task 6: Wildcards
**Purpose:** Use wildcards to match files or patterns in the script. Examples include:
- `*`: Matches zero or more characters.
- `?`: Matches exactly one character.

## Script: `shell_scripting_challenge.sh`
Below is the content of the shell script:

```bash
#!/bin/bash
# Shell Scripting Challenge

# Task 1: Comments
# This script demonstrates the use of comments, echo, variables, built-in variables, and wildcards.

# Task 2: Echo
# Using echo to print messages to the terminal.
echo "Welcome to the Shell Scripting Challenge!"

# Task 3: Variables
# Defining variables
greeting="Hello"
name="User"
today=$(date '+%Y-%m-%d') # Current date
files_count=$(ls | wc -l) # Number of files in the current directory

# Task 4: Using Variables
# Displaying the values of the variables
echo "$greeting, $name!"
echo "Today's date is: $today"
echo "Number of files in the current directory: $files_count"

# Task 5: Using Built-in Variables
# Displaying built-in variables
echo "Script name: $0"    # Name of the script
echo "Number of arguments passed: $#"
echo "Arguments passed: $@"
echo "Current working directory: $PWD"
echo "Home directory: $HOME"

# Task 6: Wildcards
# Using wildcards to list specific files
echo "Listing all shell scripts (*.sh) in the current directory:"
ls *.sh 2>/dev/null # Suppresses errors if no .sh files are found

# End of script
echo "Shell Scripting Challenge completed!"
```

## How to Run the Script

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo-name.git
    ```
2. Navigate to the directory:
    ```bash
    cd your-repo-name
    ```
3. Make the script executable:
    ```bash
    chmod +x shell_scripting_challenge.sh
    ```
4. Run the script:
    ```bash
    ./shell_scripting_challenge.sh
    ```
5. Optionally, pass arguments to test built-in variables:
    ```bash
    ./shell_scripting_challenge.sh arg1 arg2
    ```

## Key Concepts Demonstrated

- **Comments:** Adding documentation to your script.
- **Echo:** Displaying text and variable values.
- **Variables:** Storing reusable data in the script.
- **Built-in Variables:** Accessing Bash-provided information.
- **Wildcards:** Matching file patterns in the directory.

