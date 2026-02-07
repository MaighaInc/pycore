"""
Advanced Assignment 4: Directory Organizer

Scenario:
Organize files by extension and add version suffix if duplicates exist.

Objective:
Implement recursive organization with safe file moves.

Tasks:
1. Create a folder "workspace_advanced" with sample files in nested folders
2. Scan all files recursively
3. Move files into extension folders under "organized"
4. If a file name already exists, append _1, _2, ...
5. Print the final moved paths

Hints:
- Use Path.rglob("*")
- Use Path.stem and Path.suffix
- Check if destination exists before moving

Rubric:
- Correct recursive scan: 30%
- Correct collision handling: 30%
- Correct file moves: 30%
- Output formatting: 10%
"""

from pathlib import Path

# Your code here

