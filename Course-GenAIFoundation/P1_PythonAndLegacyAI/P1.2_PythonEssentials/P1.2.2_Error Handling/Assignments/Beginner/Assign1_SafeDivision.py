"""
Beginner Assignment 1: Safe Division Calculator

Scenario:
Create a calculator that handles division by zero gracefully.

Objective:
Use try-except to catch and handle ZeroDivisionError.

Tasks:
1. Create a function safe_divide(a, b)
2. Use try-except to catch ZeroDivisionError
3. Return the result if successful
4. Return an error message if division by zero
5. Test with multiple division operations

Inputs:
- 10 / 2
- 15 / 0
- 20 / 4
- 100 / 0

Expected Output:
10 / 2 = 5.0
15 / 0 = Error: Cannot divide by zero
20 / 4 = 5.0
100 / 0 = Error: Cannot divide by zero

Hints:
- Use try: attempt division
- Use except ZeroDivisionError: handle error
- Return different values based on success/failure

Rubric:
- Correct try-except structure: 40%
- Proper ZeroDivisionError handling: 40%
- Correct output formatting: 20%
"""

# Test cases
divisions = [
    (10, 2),
    (15, 0),
    (20, 4),
    (100, 0)
]

# Your code here

