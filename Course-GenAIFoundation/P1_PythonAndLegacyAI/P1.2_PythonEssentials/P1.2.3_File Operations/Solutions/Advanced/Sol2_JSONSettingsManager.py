"""
Solution: Advanced Assignment 2 - JSON Settings Manager
"""

import json

# Input data
default_settings = {
    "ui": {"theme": "light", "font": {"size": 12}},
    "notifications": {"email": True, "sms": False}
}
user_settings = {
    "ui": {"theme": "dark", "font": {"size": 14}},
    "notifications": {"sms": True}
}

def deep_merge(base, updates):
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(base.get(key), dict):
            deep_merge(base[key], value)
        else:
            base[key] = value
    return base

# Write defaults
with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(default_settings, file, indent=2)

# Load current settings
with open("settings.json", "r", encoding="utf-8") as file:
    current = json.load(file)

# Backup
with open("settings_backup.json", "w", encoding="utf-8") as file:
    json.dump(current, file, indent=2)

# Merge and save
merged = deep_merge(current, user_settings)
with open("settings_updated.json", "w", encoding="utf-8") as file:
    json.dump(merged, file, indent=2)

print(merged)
