"""
Solution: Beginner Assignment 5 - Data Access Wrapper
"""

# Test data
user_data = {"name": "Alice", "age": 25, "city": "NYC"}
keys_to_test = ["name", "email"]

def get_user_info(data, key):
    try:
        return data[key]
    except KeyError:
        return f"Key '{key}' not found"
    finally:
        print("Access attempt completed")

# Test key access
for key in keys_to_test:
    print(f"\nAccessing '{key}'")
    result = get_user_info(user_data, key)
    if not result.startswith("Key"):
        print(f"{key}: {result}")
    else:
        print(f"Error: {result}")
