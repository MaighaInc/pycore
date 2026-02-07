"""
Solution: Advanced Assignment 3 - List Access Handler
"""

# Test data
data = [
    ["apple", "banana"],
    ["carrot", "daikon", "endive"],
    ["fig"]
]
requests = [
    [0, 1],
    [1, slice(0, 2)],
    [2, 5],
    [3, 0],
    ["bad", 0]
]

class InvalidIndexError(Exception):
    pass

class AccessOutOfRangeError(Exception):
    pass

def safe_access(data, path):
    try:
        current = data
        for idx in path:
            if not isinstance(idx, (int, slice)):
                raise InvalidIndexError("Invalid index type")
            current = current[idx]
        return current
    except IndexError:
        raise AccessOutOfRangeError("Index out of range")

# Process requests
for path in requests:
    try:
        result = safe_access(data, path)
        print(f"{path} -> {result}")
    except InvalidIndexError as e:
        print(f"{path} -> Error: {e}")
    except AccessOutOfRangeError as e:
        print(f"{path} -> Error: {e}")
