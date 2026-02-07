"""
Advanced Assignment 1: Safe Division Calculator

Scenario:
A financial service performs batch divisions and needs detailed error
classification and custom exceptions.

Objective:
Implement safe division with custom exceptions and structured results.

Tasks:
1. Create custom exceptions:
   - InvalidNumberError
   - DivisionByZeroError
2. Create safe_divide(a, b) that:
   - Converts inputs to float
   - Raises custom exceptions for invalid input or zero division
   - Returns result on success
3. Create process_divisions(divisions) that returns list of results
   - Each result: {"a": a, "b": b, "success": bool, "value": result_or_error}
4. Print a formatted report

Inputs:
divisions = [
    ("10", "2"),
    ("15", "0"),
    ("abc", "5"),
    ("20", "4"),
    ("7.5", "2.5")
]

Expected Output (sample):
10 / 2 = 5.0
15 / 0 = Error: Division by zero
abc / 5 = Error: Invalid number
20 / 4 = 5.0
7.5 / 2.5 = 3.0

Hints:
- Use custom exception classes
- Use try/except in process_divisions
- Keep safe_divide focused on logic

Rubric:
- Proper custom exceptions: 30%
- Correct error classification: 30%
- Clean processing pipeline: 20%
- Output formatting: 20%
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

