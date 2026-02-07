"""
Solution: Advanced Assignment 4 - Dictionary Key Checker
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

def resolve_path(data, path_tokens):
    try:
        current = data
        for token in path_tokens:
            current = current[token]
        return current
    except KeyError:
        return "Error: Key not found"
    except IndexError:
        return "Error: Index out of range"
    except TypeError:
        return "Error: Invalid path"

# Process paths
for path in paths:
    print(f"{path} -> {resolve_path(data, path)}")
