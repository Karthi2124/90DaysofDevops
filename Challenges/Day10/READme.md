# 📄 Log Analyzer and Report Generator

## 📌 Scenario
As a **system administrator**, you manage multiple servers generating daily log files. These logs contain **critical system events and errors**. This Bash script automates **log file analysis**, extracts key information, and generates a structured summary report.

## 🚀 Features
✅ **Takes a log file path as an argument**  
✅ **Counts total error messages (`ERROR` or `Failed`)**  
✅ **Finds `CRITICAL` events with line numbers**  
✅ **Identifies the top 5 most frequent error messages**  
✅ **Generates a structured report** with insights  
✅ **Moves processed log files to an archive directory**  

## 📜 Usage
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/log-analyzer.git
cd log-analyzer
```
### **2️⃣ Give Execute Permission**
```bash
chmod +x log_analyzer.sh
```
### **3️⃣ Run the Script**
```bash
./log_analyzer.sh /path/to/logfile.log
```
### **Example:**
```bash
./log_analyzer.sh /var/log/syslog
```

## 📊 Output
The script generates a report file named:
```bash
log_summary_YYYY-MM-DD.txt
```
### **Report Includes:**
```txt
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

## 📂 Archiving Processed Log Files
✅ **Processed log files** are automatically **moved to the `archive/` directory**.  
✅ This **keeps logs organized** and **prevents re-processing** old files.  

## 🛠 Requirements
- Bash (Linux/macOS)
- `grep`, `awk`, `sort`, and `uniq` utilities

## 📜 License
This project is licensed under the **MIT License**.

## 🤝 Contributions
Want to improve this project? Feel free to submit issues or pull requests!

## 👤 Author
**Developed by:** Karthikeyan  
🚀 Follow me on GitHub: [yourusername](https://github.com/yourusername)  

