# Log File Parser – Security Log Analyzer

## 📌 Project Overview

**Log File Parser** is a command-line tool developed in C language to analyze text-based log files and detect suspicious activities using specific keywords.

The tool is designed to help beginner SOC (Security Operations Center) analysts understand the basics of log analysis, identify suspicious events, and extract relevant security information from system logs.

It reads log files line by line, searches for a user-defined keyword, displays matching entries with their corresponding line numbers, and generates a summary report showing the total number of lines scanned and alerts detected.

## ✨ Features

- Read text-based log files.
- Search for specific keywords in log entries.
- Display suspicious entries with accurate line numbers.
- Count the total number of detected alerts.
- Generate a final analysis report.
- Handle large files using a fixed-size memory buffer.
- Display error messages when a file cannot be opened.
- Accept log file paths and keywords through command-line arguments.

## 🛠️ Technologies Used

- **Programming Language:** C
- **Compiler:** GCC
- **Development Environment:** Visual Studio Code
- **Terminal:** MSYS2 UCRT64

## 📂 Project Structure

```text
log_file_parser/
│
├── log_parser.c
├── log_parser.exe
├── simple.log
└── README.md
```

## ⚙️ Requirements

- GCC Compiler
- MSYS2 UCRT64 or any compatible C development environment.
- Windows, Linux, or macOS.

## 🚀 Compilation

Compile the source code using GCC:

```bash
gcc -Wall -Wextra -std=c11 log_parser.c -o log_parser.exe
```

## ▶️ Usage

Run the program with two arguments:

```bash
./log_parser.exe <log_file> <keyword>
```

### Examples

Search for failed login attempts:

```bash
./log_parser.exe sample.log FAILED
```

Search for HTTP 404 errors:

```bash
./log_parser.exe sample.log 404
```

Search for system errors:

```bash
./log_parser.exe sample.log ERROR
```

## 📊 Sample Output

```text
====================================
       LOG FILE ANALYZER
====================================

Log File : simple.log
Keyword  : FAILED

------------------------------------
Suspicious Log Entries:

[ALERT] Line 2: [ERROR] Login FAILED for user root
[ALERT] Line 4: [WARNING] Multiple FAILED login attempts
[ALERT] Line 8: [ERROR] Database connection FAILED

====================================
           ANALYSIS REPORT
====================================

Total Lines Scanned : 10
Total Alerts Found  : 3
Status: Suspicious entries detected!

====================================
```

## 📚 C Functions Used

| Function | Description |
|---|---|
| `fopen()` | Opens the log file in read mode. |
| `fgets()` | Reads the file line by line. |
| `strstr()` | Searches for a keyword within a string. |
| `printf()` | Displays matching entries and reports. |
| `fclose()` | Closes the opened file. |

## 🎯 Learning Objectives

This assignment demonstrates practical use of:

- File handling in C.
- String manipulation and searching.
- Arrays and character buffers.
- Loops and conditional statements.
- Command-line arguments (`argc` and `argv`).
- Basic security log analysis concepts.

## 🔮 Future Improvements

- Support searching for multiple keywords simultaneously.
- Implement case-insensitive searching.
- Categorize alerts based on severity.
- Export analysis results to a separate report file.
- Improve handling of very long log lines.
- Add timestamps and event classification.

## 👨‍💻 Author

**Eng. Moath Al-Hazi**

---

*Developed as part of a programming training assignment.*