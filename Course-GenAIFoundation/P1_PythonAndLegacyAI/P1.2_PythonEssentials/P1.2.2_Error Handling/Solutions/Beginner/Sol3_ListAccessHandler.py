"""
Solution: Beginner Assignment 3 - List Access Handler
"""

# Test data
fruits = ["apple", "banana", "orange"]
indices = [0, 1, 5, -1, 10]

def safe_get_element(items, index):
    try:
        return items[index]
    except IndexError:
        return "Error: Index out of range"

# Process indices
for idx in indices:
    print(f"Index {idx}: {safe_get_element(fruits, idx)}")
