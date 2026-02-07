"""
Beginner Assignment 3: List Access Handler

Scenario:
Safely access list elements and handle index errors.

Objective:
Use try-except to catch IndexError when accessing list elements.

Tasks:
1. Create a function safe_get_element(list, index)
2. Try to access the element at given index
3. Catch IndexError and return appropriate message
4. Test with valid and invalid indices

Inputs:
fruits = ["apple", "banana", "orange"]
Indices to test: 0, 1, 5, -1, 10

Expected Output:
Index 0: apple
Index 1: banana
Index 5: Error: Index out of range
Index -1: orange
Index 10: Error: Index out of range

Hints:
- Try accessing list[index]
- Catch IndexError exception
- Negative indices are valid in Python

Rubric:
- Correct try-except structure: 40%
- Proper IndexError handling: 40%
- Output formatting: 20%
"""

# Test data
fruits = ["apple", "banana", "orange"]
indices = [0, 1, 5, -1, 10]

# Your code here

