"""
Solution: Advanced Assignment 1 - Temperature Converter
"""

from functools import wraps

# Input data
readings = [
    ("Morning", 68, "F", "C"),
    ("Noon", 295.15, "K", "C"),
    ("Evening", 22, "C", "F"),
    ("Night", 60, "F", "K"),
    ("Repeat", 68, "F", "C")
]

def log_conversion(func):
    """Decorator to log conversions."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        result, cached = func(*args, **kwargs)
        value, from_unit, to_unit = args
        suffix = " (cached)" if cached else ""
        print(f"[LOG] {from_unit}->{to_unit} {value} => {result:.1f}{suffix}")
        return result
    return wrapper

def cache_results(func):
    """Decorator to cache conversion results."""
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args], True
        result = func(*args, **kwargs)
        cache[args] = result
        return result, False
    return wrapper

@log_conversion
@cache_results
def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Convert to Celsius
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return None  # Unknown unit

    # Convert from Celsius
    if to_unit == "C":
        return celsius
    if to_unit == "F":
        return (celsius * 9 / 5) + 32
    if to_unit == "K":
        return celsius + 273.15

    return None  # Unknown unit

# Process readings
for _, value, from_unit, to_unit in readings:
    convert_temperature(value, from_unit, to_unit)
