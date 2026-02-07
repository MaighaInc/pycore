"""
Intermediate Assignment 5: Log File Handler

Scenario:
Parse a log file and count log levels.

Objective:
Practice file reading and text processing.

Tasks:
1. Write log entries to "system.log"
2. Read the file and count INFO, WARNING, ERROR
3. Write a summary file "log_summary.txt"
4. Print the summary

Inputs:
logs = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found",
    "2026-02-07 10:12:45 INFO User login"
]

Expected Output:
INFO: 2
WARNING: 1
ERROR: 1

Hints:
- Use split() to extract log level
- Use dict for counting

Rubric:
- Correct parsing: 40%
- Correct counting: 40%
- Output formatting: 20%
"""

# Input data
logs = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found",
    "2026-02-07 10:12:45 INFO User login"
]

# Your code here

