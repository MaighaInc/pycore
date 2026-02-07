"""
Advanced Assignment 3: List Access Handler

Scenario:
Access nested lists with mixed indices and slicing safely.

Objective:
Create a robust accessor with detailed error messages.

Tasks:
1. Create safe_access(data, path)
   - path is a list of indices or slices, e.g., [0, 1] or [1, slice(0, 2)]
2. Raise custom errors for invalid access
3. Return value or error message
4. Test with provided cases

Inputs:
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

Expected Output (sample):
[0, 1] -> banana
[1, slice(0, 2, None)] -> ['carrot', 'daikon']
[2, 5] -> Error: Index out of range
[3, 0] -> Error: Index out of range
['bad', 0] -> Error: Invalid index type

Hints:
- Use isinstance(idx, int) or isinstance(idx, slice)
- Catch IndexError and TypeError
- Provide clear error messages

Rubric:
- Correct traversal logic: 40%
- Proper error handling: 40%
- Output formatting: 20%
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

# Your code here

