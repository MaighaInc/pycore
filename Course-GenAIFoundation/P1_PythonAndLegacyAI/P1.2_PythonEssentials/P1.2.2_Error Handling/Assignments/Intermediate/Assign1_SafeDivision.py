"""
Intermediate Assignment 1: Safe Division Calculator

Scenario:
Your API receives numeric inputs as strings. Build a safe division utility
that handles invalid inputs and division errors.

Objective:
Use try/except/else/finally to safely divide values.

Tasks:
1. Create a function safe_divide(a, b)
   - Convert inputs to float
   - Catch ValueError and ZeroDivisionError
   - Return a tuple: (success, result_or_message)
2. Process a list of division requests
3. Print formatted output for each request

Inputs:
divisions = [
    ("10", "2"),
    ("15", "0"),
    ("abc", "5"),
    ("20", "4"),
    ("7.5", "2.5")
]

Expected Output:
10 / 2 = 5.0
15 / 0 = Error: Cannot divide by zero
abc / 5 = Error: Invalid number
20 / 4 = 5.0
7.5 / 2.5 = 3.0

Hints:
- Use float() conversion
- Use else block for successful division
- Use finally to log completion (optional)

Rubric:
- Correct error handling: 40%
- Proper conversion logic: 30%
- Clear output formatting: 30%
"""

# Test cases
divisions = [
    ("10", "2"),
    ("15", "0"),
    ("abc", "5"),
    ("20", "4"),
    ("7.5", "2.5")
]

# Your code here

