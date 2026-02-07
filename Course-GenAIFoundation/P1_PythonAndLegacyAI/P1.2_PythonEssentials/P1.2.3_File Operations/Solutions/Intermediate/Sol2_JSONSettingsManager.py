"""
Solution: Intermediate Assignment 2 - JSON Settings Manager
"""

import json

# Input data
default_settings = {
    "theme": "light",
    "font_size": 12,
    "notifications": True,
    "language": "en"
}
user_settings = {
    "theme": "dark",
    "font_size": 14
}

# Write default settings
with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(default_settings, file)

# Read and update
with open("settings.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

loaded.update(user_settings)

# Write updated settings
with open("settings_updated.json", "w", encoding="utf-8") as file:
    json.dump(loaded, file, indent=2)

print(loaded)
