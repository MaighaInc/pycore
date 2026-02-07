"""
Solution: Advanced Assignment 1 - Text File Report
"""

# Input data
report_lines = [
    "Date: 2026-02-07",
    "Mood: Productive",
    "Tasks: 5",
    "Notes: Reviewed Python basics and file operations",
    "Notes: File operations practice and review"
]

filename = "daily_report.txt"
summary_file = "report_summary.txt"

# Write file
with open(filename, "w", encoding="utf-8") as file:
    file.write("\n".join(report_lines))

# Read and analyze
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

lines = content.splitlines()
words = [w.strip(":,.!?" ).lower() for w in content.split()]

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Top 3 words
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]

summary = [
    f"Lines: {len(lines)}",
    f"Words: {len(words)}",
    "Top words: " + ", ".join(f"{w}({c})" for w, c in top_words)
]

# Write summary
with open(summary_file, "w", encoding="utf-8") as file:
    file.write("\n".join(summary))

# Print summary
print("\n".join(summary))
