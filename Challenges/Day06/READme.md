
# Linux File Permissions and Access Control

## 1. Understanding File Permissions

### Step 1: Create a File and View Details

Create a file:
```bash
touch example.txt
```

View file details:
```bash
ls -ltr
```

Note the default permissions (`-rw-r--r--`).

### Step 2: Change Ownership

Change the owner using `chown`:
```bash
sudo chown <new_owner> example.txt
```

Verify the changes:
```bash
ls -ltr
```

### Step 3: Change Group

Change the group using `chgrp`:
```bash
sudo chgrp <new_group> example.txt
```

Verify the changes:
```bash
ls -ltr
```

### Step 4: Change Other Users’ Permissions

Modify permissions using `chmod`:
```bash
chmod o+w example.txt
```

Note the changes in permissions using `ls -ltr`.

---

## 2. Writing an Article About File Permissions

### Include the Following:

- The significance of file permissions.
- Explanation of Owner, Group, and Others.
- How `chmod`, `chown`, and `chgrp` work.
- Examples demonstrating changes in permissions.

---

## 3. Access Control Lists (ACL)

### Step 1: Read About ACL

**Commands to know:**
- `getfacl`: Displays ACL for files/directories.
- `setfacl`: Sets ACL permissions.

### Step 2: Practical Task

1. Create a directory:
    ```bash
    mkdir acl_test
    ```

2. Set ACL permissions:
    ```bash
    setfacl -m u:<user>:rwx acl_test
    setfacl -m g:<group>:r acl_test
    ```

3. Verify permissions:
    ```bash
    getfacl acl_test
    ```

---

## 4. Additional Tasks

### Task 1: Script to Change Permissions of Multiple Files

Create a script `change_permissions.sh`:

```bash
read -p "Enter directory path: " dir
read -p "Enter permissions (e.g., 755): " perms
for file in "$dir"/*; do
    chmod $perms "$file"
done
echo "Permissions updated for files in $dir"
```

Run the script:
```bash
bash change_permissions.sh
```

### Task 2: Script to Set ACL Permissions

Create a script `set_acl_permissions.sh`:

```bash
read -p "Enter file path: " file
read -p "Enter username: " user
read -p "Enter ACL permissions (e.g., rwx): " perms
setfacl -m u:$user:$perms "$file"
echo "ACL permissions set for $user on $file"
```

Run the script:
```bash
bash set_acl_permissions.sh
```

---

## 5. Understanding Sticky Bit, SUID, and SGID

### Sticky Bit

Prevents users from deleting files they don’t own in a shared directory.

Example:
```bash
mkdir sticky_test
chmod +t sticky_test
ls -ld sticky_test
```

### SUID (Set User ID)

Allows a program to run with the file owner's permissions.

Example:
```bash
chmod u+s example.txt
ls -l example.txt
```

### SGID (Set Group ID)

Ensures new files in a directory inherit the group ownership.

Example:
```bash
chmod g+s sticky_test
ls -ld sticky_test
```

---

## 6. Backup and Restore Permissions

### Task 1: Backup Permissions

Create `backup_permissions.sh`:

```bash
read -p "Enter directory path: " dir
getfacl -R "$dir" > permissions_backup.acl
echo "Permissions backed up to permissions_backup.acl"
```

### Task 2: Restore Permissions

Create `restore_permissions.sh`:

```bash
read -p "Enter backup file path: " backup
setfacl --restore="$backup"
echo "Permissions restored from $backup"
```

Run the scripts to backup and restore permissions:
```bash
bash backup_permissions.sh
bash restore_permissions.sh
