# Backup with Rotation Script

This Bash script automates the process of creating backups of files in a directory, organizes them with timestamped folders, and manages backup rotation to retain only the latest backups. Perfect for DevOps engineers or anyone needing efficient and automated file backup management.

---

## Features

- **Timestamped Backups**: Creates unique backup folders with timestamps, ensuring backups are well-organized and never overwritten.
- **Backup Rotation**: Retains only the last three backups, deleting older ones automatically to save storage space.
- **Simple Usage**: Takes the directory path as an argument, making it flexible and easy to use.

---

## How It Works

1. **Automating Backups with Timestamps**
   - The script creates a backup folder named `backup_<timestamp>` where `<timestamp>` follows the format `YYYY-MM-DD_HH-MM-SS`.
   - It copies all the files from the specified directory into this timestamped folder.

2. **Backup Rotation**
   - After creating a backup, the script checks the number of backup folders.
   - If more than three backups exist, the oldest one is deleted, ensuring only the latest three backups are retained.

---

## Script Details

### **Code**

```bash

if [ -z "$1" ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

directory_path=$1


timestamp=$(date +'%Y-%m-%d_%H-%M-%S')
backup_dir="${directory_path}/backup_${timestamp}"


mkdir -p "$backup_dir"
cp -r "${directory_path}"/* "$backup_dir"
echo "Backup created: $backup_dir"

backup_folders=($(ls -dt ${directory_path}/backup_*))

while [ "${#backup_folders[@]}" -gt 3 ]; do
  oldest_backup="${backup_folders[-1]}"
  rm -rf "$oldest_backup"
  echo "Deleted old backup: $oldest_backup"
 
  backup_folders=("${backup_folders[@]:0:${#backup_folders[@]}-1}")
done
