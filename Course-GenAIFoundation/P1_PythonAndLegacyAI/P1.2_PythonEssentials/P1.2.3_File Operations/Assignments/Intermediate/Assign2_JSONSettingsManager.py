"""
Intermediate Assignment 2: JSON Settings Manager

Scenario:
Merge user settings with defaults and save a formatted JSON file.

Objective:
Practice JSON loading, updating, and pretty printing.

Tasks:
1. Save default settings to "settings.json"
2. Load the file, update with user_settings
3. Save updated settings to "settings_updated.json" (pretty format)
4. Print the updated settings

Inputs:
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

Expected Output:
Updated settings printed with merged values.

Hints:
- Use dict.update()
- Use json.dump(..., indent=2)

Rubric:
- Correct JSON read/write: 40%
- Correct merge logic: 40%
- Output formatting: 20%
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

# Your code here

