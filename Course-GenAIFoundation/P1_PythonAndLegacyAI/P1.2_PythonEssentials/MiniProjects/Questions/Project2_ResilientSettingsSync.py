"""
Mini Project 2: Resilient Settings Sync
Level: Intermediate

Concepts Used:
- Functions and docstrings
- Error handling (custom exceptions, retries)
- JSON file operations
- Async programming (retry with delay)

Description:
Build a settings sync tool that loads local settings, merges with defaults,
then saves updates with retry logic.

Expected Output (sample):
==================================================
SETTINGS SYNC
==================================================
Loaded settings.json
Merged settings
Save succeeded on attempt 2
==================================================
"""

import asyncio
import json

# Default and user settings - DO NOT MODIFY
DEFAULT_SETTINGS = {
    "ui": {"theme": "light", "font": {"size": 12}},
    "notifications": {"email": True, "sms": False}
}
USER_SETTINGS = {
    "ui": {"theme": "dark", "font": {"size": 14}},
    "notifications": {"sms": True}
}

print("=" * 50)
print("SETTINGS SYNC")
print("=" * 50)

# TODO: Step 1 - Write DEFAULT_SETTINGS to settings.json

# TODO: Step 2 - Implement deep_merge(base, updates)

# TODO: Step 3 - Implement async save_with_retries(filename, data, max_retries)
# - Use asyncio.sleep for delay
# - Catch exceptions and retry

# TODO: Step 4 - Implement sync workflow in async main()
# - Load settings.json
# - Merge with USER_SETTINGS
# - Save with retries

# YOUR CODE HERE

