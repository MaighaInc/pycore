"""
Solution: Advanced Assignment 4 - Directory Organizer
"""

from pathlib import Path

root = Path("workspace_advanced")
organized = root / "organized"

# Create sample nested files
(root / "a").mkdir(parents=True, exist_ok=True)
(root / "b").mkdir(parents=True, exist_ok=True)
(root / "a" / "report.txt").write_text("sample", encoding="utf-8")
(root / "b" / "report.txt").write_text("sample", encoding="utf-8")
(root / "b" / "data.csv").write_text("sample", encoding="utf-8")
(root / "b" / "image.png").write_text("sample", encoding="utf-8")

organized.mkdir(parents=True, exist_ok=True)

# Move files
for file_path in root.rglob("*"):
    if file_path.is_file() and "organized" not in file_path.parts:
        ext = file_path.suffix.lstrip(".") or "no_ext"
        target_dir = organized / ext
        target_dir.mkdir(parents=True, exist_ok=True)

        target = target_dir / file_path.name
        counter = 1
        while target.exists():
            target = target_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
            counter += 1

        file_path.rename(target)
        print(target)
