"""
Solution: Beginner Assignment 4 - Directory Organizer
"""

from pathlib import Path

root = Path("project_files")
subfolders = ["docs", "data", "logs"]

for folder in subfolders:
    path = root / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created: {path}")
