"""
Solution: Advanced Assignment 5 - Log File Handler
"""

# Input data
logs = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found",
    "2026-02-07 10:11:05 ERROR Database timeout",
    "2026-02-07 10:12:45 INFO User login"
]

# Write logs
with open("system.log", "w", encoding="utf-8") as file:
    file.write("\n".join(logs))

# Filter errors
errors = []
with open("system.log", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split(" ", 3)
        if len(parts) >= 4 and parts[2] == "ERROR":
            errors.append(parts[3].strip())

# Write error report
with open("error_report.txt", "w", encoding="utf-8") as file:
    for err in errors:
        file.write(err + "\n")

# Print summary
print(f"Total errors: {len(errors)}")
if errors:
    print(f"First error: {errors[0]}")
