"""
Solution: Intermediate Assignment 1 - Text File Report
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

filename = "daily_report.txt"

# Write initial content
with open(filename, "w", encoding="utf-8") as file:
    file.write("\n".join(initial_lines))

# Append new notes
with open(filename, "a", encoding="utf-8") as file:
    file.write("\n" + "\n".join(new_notes))

# Read and compute stats
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
lines = content.splitlines()
words = content.split()

print(f"Lines: {len(lines)}")
print(f"Words: {len(words)}")
