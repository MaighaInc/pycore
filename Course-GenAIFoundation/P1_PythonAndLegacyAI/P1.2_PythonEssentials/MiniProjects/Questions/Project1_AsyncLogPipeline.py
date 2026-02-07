"""
Mini Project 1: Async Log Processing Pipeline
Level: Intermediate

Concepts Used:
- Functions (helpers, composition)
- Error handling (try/except)
- File operations (read/write)
- Async programming (async/await, gather)

Description:
Build an async pipeline that writes log data to a file, reads it back,
parses log levels, and writes a summary report.

Expected Output (sample):
==================================================
ASYNC LOG PIPELINE
==================================================
Total logs: 6
INFO: 3
WARNING: 1
ERROR: 2
Summary saved to: log_summary.txt
==================================================
"""

import asyncio

# Sample log data - DO NOT MODIFY
log_data = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found",
    "2026-02-07 10:12:45 INFO User login",
    "2026-02-07 10:15:10 ERROR Database timeout",
    "2026-02-07 10:20:00 INFO Job completed"
]

print("=" * 50)
print("ASYNC LOG PIPELINE")
print("=" * 50)

# TODO: Step 1 - Write logs to "system.log"
# - Create an async function write_logs(filename, lines)
# - Use asyncio.to_thread to write file

# TODO: Step 2 - Read logs from file asynchronously
# - Create async function read_logs(filename)
# - Return list of lines

# TODO: Step 3 - Parse log levels
# - Create function count_levels(lines)
# - Return dict with counts

# TODO: Step 4 - Write summary report to "log_summary.txt"
# - Include total count and level counts

# TODO: Step 5 - Create async main() to run steps

# YOUR CODE HERE

