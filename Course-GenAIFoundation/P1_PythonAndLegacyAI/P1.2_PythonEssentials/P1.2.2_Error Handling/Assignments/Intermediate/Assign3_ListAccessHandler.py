"""
Intermediate Assignment 3: List Access Handler

Scenario:
Safely access nested lists while handling out-of-range and type errors.

Objective:
Build a safe getter that supports nested list access.

Tasks:
1. Create safe_get(list_obj, index, *, default="N/A")
2. Create safe_get_nested(list_obj, indices)
   - indices is a list of indexes to traverse
3. Handle IndexError and TypeError
4. Test with provided data

Inputs:
data = [
    ["apple", "banana"],
    ["carrot", "daikon"],
    ["eggplant"]
]
requests = [
    ([0], 1),       # banana
    ([1], 0),       # carrot
    ([2], 1),       # out of range
    ([3], 0),       # out of range
    ("bad", 0)      # type error
]

Expected Output:
[0][1] -> banana
[1][0] -> carrot
[2][1] -> Error: Index out of range
[3][0] -> Error: Index out of range
bad[0] -> Error: Invalid list structure

Hints:
- Use isinstance(list_obj, list)
- Wrap access in try/except
- Return consistent error messages

Rubric:
- Correct nested access logic: 40%
- Proper exception handling: 40%
- Output formatting: 20%
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

# Your code here

