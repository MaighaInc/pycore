"""
Advanced Assignment 5: Data Access Wrapper

Scenario:
Load nested configuration from dictionaries with robust error handling and fallback.

Objective:
Implement safe nested data access with detailed exception handling.

Tasks:
1. Create get_config(config_dict, path, default)
   - path is a list of keys (e.g., ["database", "host"])
   - Navigate nested dicts using the path
2. Handle:
   - KeyError (missing key)
   - TypeError (non-dict encountered)
   - IndexError (invalid path)
3. Return value if found, else default
4. Print a clear status message per config

Inputs:
configs = [
    {"database": {"host": "localhost", "port": 5432}},
    {"database": {"host": "remote.com"}},
    {"cache": {"ttl": 300}},
    None
]

paths = [
    ["database", "host"],
    ["database", "port"],
    ["database", "host"],
    ["database", "host"]
]

default_value = "default"

Expected Output:
Config 0, path database.host -> localhost
Config 1, path database.port -> default (KeyError)
Config 2, path database.host -> default (KeyError)
Config 3, path database.host -> default (TypeError)

Hints:
- Iterate through path keys
- Use try/except for each access
- Handle None as TypeError

Rubric:
- Correct exception handling: 40%
- Proper fallback behavior: 30%
- Clean function structure: 20%
- Output formatting: 10%
"""

# Test data
configs = [
    {"database": {"host": "localhost", "port": 5432}},
    {"database": {"host": "remote.com"}},
    {"cache": {"ttl": 300}},
    None
]

paths = [
    ["database", "host"],
    ["database", "port"],
    ["database", "host"],
    ["database", "host"]
]

default_value = "default"

# Your code here

