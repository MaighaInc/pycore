"""
Solution: Beginner Assignment 1 - Text File Report
"""

# Input data
report_lines = [
    "Date: 2026-02-07",
    "Mood: Productive",
    "Tasks: 5",
    "Notes: Reviewed Python basics"
]

filename = "daily_report.txt"

# Write file
with open(filename, "w", encoding="utf-8") as file:
    file.write("\n".join(report_lines))

# Read file
with open(filename, "r", encoding="utf-8") as file:
    contents = file.read()

print(contents)
