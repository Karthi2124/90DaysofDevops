# Day 28 – Revision Day

##  Self-Assessment

### Linux

* File system navigation →  Confident
* Process management →  Confident
* systemd services →  Need to revisit
* Text editors (vim/nano) →  Confident
* Resource troubleshooting →  Need to revisit
* File system hierarchy →  Confident
* Users & groups →  Confident
* Permissions (chmod) →  Confident
* Ownership (chown/chgrp) →  Confident
* LVM →  Need to revisit
* Networking tools →  Need to revisit
* DNS & ports →  Need to revisit

---

### Shell Scripting

* Variables & arguments → ✅
* Conditions (if/case) → ✅
* Loops → ✅
* Functions →  Need practice
* Text processing →  Need practice
* Error handling →  Need practice
* Cron jobs → ✅

---

### Git & GitHub

* Init, commit → ✅
* Branching → ✅
* Push/Pull → ✅
* Clone vs Fork → ✅
* Merge vs Rebase →  Need clarity
* Stash → ✅
* Cherry-pick →  Need practice
* Reset vs Revert → ✅
* Branching strategies →  Need revision
* GitHub CLI → ✅

---

##  Topics Revisited

### 1. systemd Services

* Learned how to start/stop services
* Used: `systemctl start`, `stop`, `status`

### 2. LVM

* Understood PV → VG → LV structure
* Helps in flexible disk resizing

### 3. Merge vs Rebase

* Merge → keeps history
* Rebase → creates clean linear history

---

##  Quick-Fire Answers

**1. chmod 755 script.sh**
Gives read, write, execute to owner and read/execute to others.

**2. Process vs Service**
Process = running program
Service = background process managed by system

**3. Port 8080 usage**

```bash
lsof -i :8080
```

**4. set -euo pipefail**

* e → exit on error
* u → undefined variable error
* pipefail → fail pipeline if any command fails

**5. reset --hard vs revert**
reset --hard → deletes history (dangerous)
revert → creates new undo commit (safe)

**6. Best strategy for 5 devs**
GitHub Flow

**7. git stash**
Temporarily saves uncommitted work

**8. Cron job (3 AM)**

```bash
0 3 * * * /path/script.sh
```

**9. fetch vs pull**
fetch → download only
pull → download + merge

**10. LVM**
Flexible disk management (resize easily)

---

##  Work Check

* All days (1–27) pushed 
* git-commands.md updated 
* Shell cheat sheet completed 
* GitHub profile cleaned 

---

##  Teaching Section

### Git Branching (Simple Explanation)

Git branching allows you to create separate versions of your code.
Each branch works independently, so you can build features without breaking the main code.
Once the work is done, you merge it back into the main branch.
This helps teams work safely and efficiently.

---

##  Key Takeaways

* Linux + Git are foundational DevOps skills
* Practice matters more than theory
* Mistakes (merge conflicts, resets) are part of learning
* Confidence comes from doing, not reading

---
