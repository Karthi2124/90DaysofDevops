#  Log Analyzer and Report Generator

##  Scenario
As a **system administrator**, you need to analyze log files daily. Logs contain **error messages, critical events, and warnings** that help monitor system health.

Instead of manually checking logs, this **Bash script automates** the entire process:
- Reads a log file.
- Counts errors.
- Finds critical issues.
- Summarizes findings in a structured report.

---

## Features
**Accepts log file path as input**  
**Counts total error messages (`ERROR` or `Failed`)**  
**Finds `CRITICAL` events with line numbers**  
**Identifies the top 5 most frequent error messages**  
**Generates a structured report**  
**Moves processed log files to an archive directory**  

---

## Steps to Implement
### **1️Accept Log File as Input**
The script takes a log file path as a command-line argument.
```bash
./log_analyzer.sh /var/log/syslog
```
This processes the given log file.

### **2️Count Error Messages**
- The script searches for error messages (`ERROR` or `Failed`).
- It counts how many times errors appear in the log.
```bash
grep -E 'ERROR|Failed' logfile.log | wc -l
```

### **3️Find Critical Events**
- Searches for `"CRITICAL"` messages.
- Displays their line numbers.
```bash
grep -n 'CRITICAL' logfile.log
```
Example output:
```
120: CRITICAL - System crash detected
340: CRITICAL - Kernel panic occurred
```

### **4️Identify the Top 5 Most Common Errors**
- Finds the most frequent error messages.
```bash
grep 'ERROR' logfile.log | sort | uniq -c | sort -nr | head -5
```
Example output:
```
45 Authentication failed for user
38 Connection timeout
30 Failed to start service
22 Unable to mount filesystem
20 Disk quota exceeded
```

### **5️Generate a Summary Report**
The script writes a structured report to a separate file (`log_summary_YYYY-MM-DD.txt`).
```
Date of Analysis: 2025-01-30
Log File: /var/log/syslog
Total Lines Processed: 10500
Total Error Count: 320
Top 5 Error Messages:
  45 Authentication failed for user
  38 Connection timeout
  30 Failed to start service
  22 Unable to mount filesystem
  20 Disk quota exceeded
Critical Events:
  Line 230: CRITICAL - System crash detected
  Line 1200: CRITICAL - Kernel panic occurred
```

### **6️ Optional - Archive Log Files**
To keep logs organized, the script can move processed log files to an `archive/` directory.
```bash
mv logfile.log archive/
```

---

## Why Use This?
- **Saves time**: No manual log checking.
- **Automates reporting**: Daily summaries generated automatically.
- **Identifies critical issues**: Helps prioritize system fixes.
- **Keeps logs organized**: Archives old logs for future reference.

---



