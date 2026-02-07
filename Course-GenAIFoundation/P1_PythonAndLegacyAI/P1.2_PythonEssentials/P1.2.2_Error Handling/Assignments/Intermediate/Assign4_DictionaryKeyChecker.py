"""
Intermediate Assignment 4: Dictionary Key Checker

Scenario:
Access nested dictionary values using a dotted path and handle missing keys.

Objective:
Create a safe getter for nested dictionaries.

Tasks:
1. Create safe_get_path(data, path)
   - path example: "user.profile.email"
2. Return value if found; otherwise return "Key not found"
3. Handle TypeError when path tries to access non-dict
4. Test with provided paths

Inputs:
user_data = {
    "user": {
        "profile": {
            "name": "Alice",
            "email": "alice@mail.com"
        },
        "settings": {
            "theme": "dark"
        }
    }
}
paths = ["user.profile.name", "user.profile.age", "user.settings.theme", "user.profile.email"]

Expected Output:
user.profile.name -> Alice
user.profile.age -> Key not found
user.settings.theme -> dark
user.profile.email -> alice@mail.com

Hints:
- Split path with .split('.')
- Traverse dictionary step by step
- Use try/except KeyError, TypeError

Rubric:
- Correct path traversal: 40%
- Proper exception handling: 40%
- Output formatting: 20%
"""

# Test data
user_data = {
    "user": {
        "profile": {
            "name": "Alice",
            "email": "alice@mail.com"
        },
        "settings": {
            "theme": "dark"
        }
    }
}
paths = ["user.profile.name", "user.profile.age", "user.settings.theme", "user.profile.email"]

# Your code here

