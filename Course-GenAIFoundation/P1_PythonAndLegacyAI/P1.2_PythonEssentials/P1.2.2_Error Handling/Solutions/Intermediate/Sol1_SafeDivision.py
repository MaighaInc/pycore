"""
Solution: Intermediate Assignment 1 - Safe Division Calculator
"""

# Test cases
divisions = [
    ("10", "2"),
    ("15", "0"),
    ("abc", "5"),
    ("20", "4"),
    ("7.5", "2.5")
]

def safe_divide(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        result = num_a / num_b
    except ValueError:
        return False, "Error: Invalid number"
    except ZeroDivisionError:
        return False, "Error: Cannot divide by zero"
    else:
        return True, result

# Process divisions
for a, b in divisions:
    success, result = safe_divide(a, b)
    print(f"{a} / {b} = {result}")
