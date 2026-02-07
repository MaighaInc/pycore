"""
Beginner Assignment 2: JSON Settings Manager

Scenario:
Save and load app settings using JSON.

Objective:
Practice json.dump and json.load.

Tasks:
1. Create a settings dictionary
2. Write it to "settings.json"
3. Read it back from the file
4. Print the loaded settings

Inputs:
settings = {
    "theme": "dark",
    "font_size": 14,
    "notifications": True
}

Expected Output:
Loaded settings: {'theme': 'dark', 'font_size': 14, 'notifications': True}

Hints:
- import json
- Use json.dump() and json.load()

Rubric:
- Correct JSON write: 40%
- Correct JSON read: 40%
- Output formatting: 20%
"""

import json

# Input data
settings = {
    "theme": "dark",
    "font_size": 14,
    "notifications": True
}

# Your code here

