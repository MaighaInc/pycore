"""
Beginner Assignment 4: Dictionary Key Checker

Scenario:
Safely retrieve values from a dictionary without crashing on missing keys.

Objective:
Use try-except to handle KeyError when accessing dictionary values.

Tasks:
1. Create a function safe_get_value(dictionary, key)
2. Try to get value for the given key
3. Catch KeyError and return default message
4. Test with existing and non-existing keys

Input:
user_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
Keys to test: "name", "age", "country", "email"

Expected Output:
Key 'name': Alice
Key 'age': 30
Key 'country': Key not found
Key 'email': Key not found

Hints:
- Use try-except KeyError
- Alternative: use .get() method
- Return appropriate message for missing keys

Rubric:
- Correct try-except KeyError: 40%
- Proper error handling: 40%
- Output formatting: 20%
"""

# Test data
user_data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
keys_to_test = ["name", "age", "country", "email"]

# Your code here

