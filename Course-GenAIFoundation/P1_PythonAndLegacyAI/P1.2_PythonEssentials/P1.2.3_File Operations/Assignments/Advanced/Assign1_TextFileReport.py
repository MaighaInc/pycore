"""
Advanced Assignment 1: Text File Report

Scenario:
Generate an analytics report from a text file, including word frequency.

Objective:
Use file reading and text processing to create a summary report.

Tasks:
1. Write content to "daily_report.txt"
2. Read the file and compute:
   - line count
   - word count
   - top 3 most common words (case-insensitive)
3. Write a summary file "report_summary.txt"
4. Print the summary

Inputs:
report_lines = [
    "Date: 2026-02-07",
    "Mood: Productive",
    "Tasks: 5",
    "Notes: Reviewed Python basics and file operations",
    "Notes: File operations practice and review"
]

Expected Output (sample):
Lines: 5
Words: 20
Top words: notes(2), file(2), operations(2)

Hints:
- Normalize words to lowercase
- Strip punctuation like ':'
- Use a dictionary to count words

Rubric:
- Correct analytics: 40%
- Correct summary file: 30%
- Output formatting: 30%
"""

# Input data
report_lines = [
    "Date: 2026-02-07",
    "Mood: Productive",
    "Tasks: 5",
    "Notes: Reviewed Python basics and file operations",
    "Notes: File operations practice and review"
]

# Your code here

