
# Day 5 Task: Advanced Linux Shell Scripting for DevOps Engineers with User Management
### 1.Create Directories Using Shell Script:

Creating directories using a shell script involves writing a script in a text file and executing it in the terminal. Below is a step-by-step explanation of how to create directories using a shell script:

#### 1. Understand the mkdir Command
mkdir (make directory) is a Linux/Unix command used to create directories.
Syntax: mkdir [options] directory_name
#### 2. Create a Shell Script
Shell scripts are text files containing commands executed by the shell interpreter.
File extensions for shell scripts are typically .sh.
#### 3. Steps to Create and Execute the Script
Step 1: Open a Terminal
Launch your terminal on Linux/Unix or a similar environment (like WSL on Windows).
Step 2: Create a Script File
Use a text editor (e.g., nano, vim, or touch) to create a file.
bash
Copy code
nano create_directories.sh
Step 3: Write the Script
Add the following content to the script file:
bash
## Copy code
> echo "Enter the name of the directory to create:"
read dir_name

echo "Enter the number of directories to create:"
read num_dirs

for ((i=1; i<=num_dirs; i++))
do
    mkdir "${dir_name}_$i"
    echo "Directory ${dir_name}_$i created"
> done 

## 2. Create a Script to Backup All Your Work:
#### Script Overview
The script will:
> Backup all files in a source directory.
> Save the backup to a destination directory.
> Add a timestamp to the backup file.
> Optionally clean old backups (e.g., older than 7 days).

