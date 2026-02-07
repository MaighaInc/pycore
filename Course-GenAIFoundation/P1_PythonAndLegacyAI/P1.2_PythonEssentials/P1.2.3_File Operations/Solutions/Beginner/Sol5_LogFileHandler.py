"""
Solution: Beginner Assignment 5 - Log File Handler
"""

# Input data
logs = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found"
]

filename = "system.log"

# Write logs
with open(filename, "w", encoding="utf-8") as file:
    file.write("\n".join(logs))

# Count lines
with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

print(f"Total log lines: {len(lines)}")
