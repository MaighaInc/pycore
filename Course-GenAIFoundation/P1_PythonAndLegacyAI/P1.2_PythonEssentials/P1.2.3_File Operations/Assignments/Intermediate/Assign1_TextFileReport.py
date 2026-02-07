"""
Intermediate Assignment 1: Text File Report

Scenario:
You need to append daily notes to an existing report and compute statistics.

Objective:
Practice appending, reading, and basic text analytics.

Tasks:
1. Write initial report lines to "daily_report.txt"
2. Append new notes to the same file
3. Read file and compute:
   - line count
   - word count
4. Print contents and statistics

Inputs:
initial_lines = [
    "Date: 2026-02-07",
    "Mood: Productive",
    "Tasks: 5"
]
new_notes = [
    "Notes: Reviewed Python basics",
    "Goals: Complete file ops module"
]

Expected Output (sample):
[File content printed...]
Lines: 5
Words: 17

Hints:
- Use open(..., "a") to append
- Use split() to count words

Rubric:
- Correct append behavior: 30%
- Correct stats calculation: 40%
- Output formatting: 30%
"""

# Input data
initial_lines = [
    "Date: 2026-02-07",
    "Mood: Productive",
    "Tasks: 5"
]
new_notes = [
    "Notes: Reviewed Python basics",
    "Goals: Complete file ops module"
]

# Your code here

