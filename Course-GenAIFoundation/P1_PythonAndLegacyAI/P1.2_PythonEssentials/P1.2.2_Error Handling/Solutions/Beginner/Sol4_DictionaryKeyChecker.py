"""
Solution: Beginner Assignment 4 - Dictionary Key Checker
"""

# Test data
user_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
keys_to_test = ["name", "age", "country", "email"]

def safe_get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "Key not found"

# Process keys
for key in keys_to_test:
    print(f"Key '{key}': {safe_get_value(user_data, key)}")
