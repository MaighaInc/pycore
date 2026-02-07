"""
Solution: Intermediate Assignment 3 - List Access Handler
"""

# Test data
data = [
    ["apple", "banana"],
    ["carrot", "daikon"],
    ["eggplant"]
]
requests = [
    ([0], 1),
    ([1], 0),
    ([2], 1),
    ([3], 0),
    ("bad", 0)
]

def safe_get(list_obj, index, *, default="N/A"):
    try:
        return list_obj[index]
    except (IndexError, TypeError):
        return default

def safe_get_nested(list_obj, indices):
    try:
        current = list_obj
        for idx in indices:
            current = current[idx]
        return current
    except IndexError:
        return "Error: Index out of range"
    except TypeError:
        return "Error: Invalid list structure"

# Process requests
for path, idx in requests:
    if isinstance(path, list):
        result = safe_get_nested(data, path + [idx])
        print(f"{path}[{idx}] -> {result}")
    else:
        result = safe_get_nested(path, [idx])
        print(f"{path}[{idx}] -> {result}")
