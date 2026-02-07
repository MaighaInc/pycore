"""
Solution: Beginner Assignment 2 - JSON Settings Manager
"""

import json

# Input data
settings = {
    "theme": "dark",
    "font_size": 14,
    "notifications": True
}

filename = "settings.json"

# Write JSON
with open(filename, "w", encoding="utf-8") as file:
    json.dump(settings, file)

# Read JSON
with open(filename, "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(f"Loaded settings: {loaded}")
