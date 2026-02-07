"""
Solution: Intermediate Assignment 4 - Dictionary Key Checker
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

def safe_get_path(data, path):
    try:
        current = data
        for part in path.split("."):
            current = current[part]
        return current
    except (KeyError, TypeError):
        return "Key not found"

# Process paths
for path in paths:
    print(f"{path} -> {safe_get_path(user_data, path)}")
