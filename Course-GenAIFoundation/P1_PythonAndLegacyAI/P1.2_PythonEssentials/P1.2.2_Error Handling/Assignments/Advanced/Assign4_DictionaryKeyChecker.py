"""
Advanced Assignment 4: Dictionary Key Checker

Scenario:
Access complex nested structures with mixed dict keys and list indices.

Objective:
Create a path resolver supporting dict keys and list indexes.

Tasks:
1. Create resolve_path(data, path_tokens)
   - path_tokens list can contain strings (dict keys) or ints (list indices)
2. Handle KeyError, IndexError, TypeError with clear messages
3. Return value or error string
4. Test with provided paths

Inputs:
data = {
    "users": [
        {"name": "Alice", "emails": ["a@mail.com", "a@work.com"]},
        {"name": "Bob", "emails": ["b@mail.com"]}
    ]
}
paths = [
    ["users", 0, "emails", 1],
    ["users", 1, "emails", 1],
    ["users", 2, "name"],
    ["users", 0, "phones", 0]
]

Expected Output (sample):
['users', 0, 'emails', 1] -> a@work.com
['users', 1, 'emails', 1] -> Error: Index out of range
['users', 2, 'name'] -> Error: Index out of range
['users', 0, 'phones', 0] -> Error: Key not found

Hints:
- Traverse tokens sequentially
- Use try/except blocks
- Validate token type before access

Rubric:
- Correct traversal: 40%
- Proper error handling: 40%
- Output formatting: 20%
"""

# Test data
data = {
    "users": [
        {"name": "Alice", "emails": ["a@mail.com", "a@work.com"]},
        {"name": "Bob", "emails": ["b@mail.com"]}
    ]
}
paths = [
    ["users", 0, "emails", 1],
    ["users", 1, "emails", 1],
    ["users", 2, "name"],
    ["users", 0, "phones", 0]
]

# Your code here

