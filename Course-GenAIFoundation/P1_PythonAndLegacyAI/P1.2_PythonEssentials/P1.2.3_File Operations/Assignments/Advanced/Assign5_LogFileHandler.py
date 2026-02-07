"""
Advanced Assignment 5: Log File Handler

Scenario:
Parse a log file, extract errors, and generate an error report.

Objective:
Combine file reading with filtering and reporting.

Tasks:
1. Write log entries to "system.log"
2. Read and filter only ERROR lines
3. Write "error_report.txt" with extracted errors
4. Print count of errors and first error message

Inputs:
logs = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found",
    "2026-02-07 10:11:05 ERROR Database timeout",
    "2026-02-07 10:12:45 INFO User login"
]

Expected Output:
Total errors: 2
First error: File not found

Hints:
- Use split() to check level
- Store error messages in a list

Rubric:
- Correct filtering: 40%
- Correct report writing: 30%
- Output formatting: 30%
"""

# Input data
logs = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found",
    "2026-02-07 10:11:05 ERROR Database timeout",
    "2026-02-07 10:12:45 INFO User login"
]

# Your code here

