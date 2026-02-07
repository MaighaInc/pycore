"""
Solution: Beginner Assignment 1 - Safe Division Calculator
"""

# Test cases
divisions = [
    (10, 2),
    (15, 0),
    (20, 4),
    (100, 0)
]

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Process divisions
for a, b in divisions:
    result = safe_divide(a, b)
    print(f"{a} / {b} = {result}")
