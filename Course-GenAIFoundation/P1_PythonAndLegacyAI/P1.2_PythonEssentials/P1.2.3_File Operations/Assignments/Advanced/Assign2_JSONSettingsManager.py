"""
Advanced Assignment 2: JSON Settings Manager

Scenario:
Manage nested JSON settings with deep merge and backups.

Objective:
Implement deep merging and create a backup of old settings.

Tasks:
1. Write default settings to "settings.json"
2. Create a deep_merge(base, updates) function
3. Load settings.json, merge user_settings
4. Save backup as "settings_backup.json"
5. Save merged result to "settings_updated.json"

Inputs:
default_settings = {
    "ui": {"theme": "light", "font": {"size": 12}},
    "notifications": {"email": True, "sms": False}
}
user_settings = {
    "ui": {"theme": "dark", "font": {"size": 14}},
    "notifications": {"sms": True}
}

Expected Output:
Updated settings printed with merged values.

Hints:
- Recursively merge dictionaries
- Use json.dump(..., indent=2)

Rubric:
- Correct deep merge: 40%
- Proper backup creation: 30%
- Output formatting: 30%
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

# Your code here

