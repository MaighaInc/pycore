"""
Solution: Intermediate Assignment 5 - Log File Handler
"""

# Input data
logs = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found",
    "2026-02-07 10:12:45 INFO User login"
]

# Write logs
with open("system.log", "w", encoding="utf-8") as file:
    file.write("\n".join(logs))

# Count levels
counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
with open("system.log", "r", encoding="utf-8") as file:
    for line in file:
        level = line.split()[2]
        if level in counts:
            counts[level] += 1

# Write summary
with open("log_summary.txt", "w", encoding="utf-8") as file:
    for level, count in counts.items():
        file.write(f"{level}: {count}\n")

# Print summary
for level, count in counts.items():
    print(f"{level}: {count}")
