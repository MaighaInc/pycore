"""
Solution: Intermediate Assignment 1 - Temperature Converter
"""

# Input data
readings = [
    ("Morning", 68, "F", "C"),
    ("Noon", 295.15, "K", "C"),
    ("Evening", 22, "C", "F"),
    ("Night", 60, "F", "K")
]

# Function definition
def convert_temperature(value, from_unit, to_unit="C"):
    """Convert temperature between C, F, K."""
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Convert to Celsius first
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return None  # Unknown unit

    # Convert from Celsius to target
    if to_unit == "C":
        return celsius
    if to_unit == "F":
        return (celsius * 9 / 5) + 32
    if to_unit == "K":
        return celsius + 273.15

    return None  # Unknown unit

# Process readings
for label, value, from_unit, to_unit in readings:
    result = convert_temperature(value, from_unit, to_unit)
    if result is not None:
        print(f"{label}: {value}{from_unit.upper()} = {result:.1f}{to_unit.upper()}")
    else:
        print(f"{label}: Error - Unknown unit")
