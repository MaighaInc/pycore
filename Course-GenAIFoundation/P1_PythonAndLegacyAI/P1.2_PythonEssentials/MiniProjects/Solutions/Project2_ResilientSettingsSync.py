"""
Mini Project 2: Resilient Settings Sync (Solution)
"""

import asyncio
import json

DEFAULT_SETTINGS = {
    "ui": {"theme": "light", "font": {"size": 12}},
    "notifications": {"email": True, "sms": False}
}
USER_SETTINGS = {
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

async def save_with_retries(filename, data, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2)
            print(f"Save succeeded on attempt {attempt}")
            return True
        except Exception:
            print(f"Save failed on attempt {attempt}")
            await asyncio.sleep(0.5)
    return False

async def main():
    print("=" * 50)
    print("SETTINGS SYNC")
    print("=" * 50)

    # Write defaults
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(DEFAULT_SETTINGS, file, indent=2)

    # Load current settings
    with open("settings.json", "r", encoding="utf-8") as file:
        current = json.load(file)
    print("Loaded settings.json")

    # Merge
    merged = deep_merge(current, USER_SETTINGS)
    print("Merged settings")

    # Save with retries
    await save_with_retries("settings_updated.json", merged, max_retries=3)
    print("=" * 50)

asyncio.run(main())
