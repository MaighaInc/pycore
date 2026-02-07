"""
Solution: Advanced Assignment 1 - Safe Division Calculator
"""

# Test cases
divisions = [
    ("10", "2"),
    ("15", "0"),
    ("abc", "5"),
    ("20", "4"),
    ("7.5", "2.5")
]

class InvalidNumberError(Exception):
    pass

class DivisionByZeroError(Exception):
    pass

def safe_divide(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
    except ValueError:
        raise InvalidNumberError("Invalid number")

    if num_b == 0:
        raise DivisionByZeroError("Division by zero")

    return num_a / num_b

def process_divisions(divisions):
    results = []
    for a, b in divisions:
        try:
            result = safe_divide(a, b)
            results.append({"a": a, "b": b, "success": True, "value": result})
        except InvalidNumberError as e:
            results.append({"a": a, "b": b, "success": False, "value": str(e)})
        except DivisionByZeroError as e:
            results.append({"a": a, "b": b, "success": False, "value": str(e)})
    return results

# Report
for item in process_divisions(divisions):
    a, b, value = item["a"], item["b"], item["value"]
    if item["success"]:
        print(f"{a} / {b} = {value}")
    else:
        print(f"{a} / {b} = Error: {value}")
