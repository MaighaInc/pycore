"""
Beginner Assignment 5: Data Access Wrapper

Scenario:
Access nested data structures safely with error handling for missing keys.

Objective:
Use try-except-finally to handle dictionary access safely.

Tasks:
1. Create a function get_user_info(data, key)
2. Try to access the key from the dictionary
3. Catch KeyError if key doesn't exist
4. Use finally to print "Access attempt completed"
5. Test with existing and non-existing keys

Expected Behavior:
- If key exists: return value
- If key doesn't exist: return "Key not found"
- Finally block always executes

Expected Output:
Accessing 'name'
name: Alice
Access attempt completed

Accessing 'email'
Error: Key 'email' not found
Access attempt completed

Hints:
- Use try-except-finally structure
- KeyError for missing keys
- finally block runs regardless of exception

Rubric:
- Correct try-except structure: 35%
- Proper KeyError handling: 35%
- Correct finally usage: 30%
"""

# Test data
user_data = {"name": "Alice", "age": 25, "city": "NYC"}
keys_to_test = ["name", "email"]

# Your code here

