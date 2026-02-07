"""
Solution: Intermediate Assignment 4 - Directory Organizer
"""

from pathlib import Path

root = Path("workspace")
root.mkdir(exist_ok=True)

# Create sample files
sample_files = ["report.txt", "data.csv", "image.png", "notes.txt"]
for name in sample_files:
    (root / name).write_text("sample", encoding="utf-8")

# Create subfolders
folders = {".txt": "txt", ".csv": "csv", ".png": "png"}
for folder in folders.values():
    (root / folder).mkdir(exist_ok=True)

# Move files
for file_path in root.iterdir():
    if file_path.is_file():
        target_folder = folders.get(file_path.suffix)
        if target_folder:
            destination = root / target_folder / file_path.name
            file_path.rename(destination)
            print(destination)
