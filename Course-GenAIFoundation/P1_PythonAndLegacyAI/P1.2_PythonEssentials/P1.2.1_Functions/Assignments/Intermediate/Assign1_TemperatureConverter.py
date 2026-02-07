"""
Intermediate Assignment 1: Temperature Converter

Scenario:
Your weather dashboard receives mixed temperature units. Convert them into
requested target units using reusable functions and default parameters.

Objective:
Create a flexible conversion function that supports C, F, and K.

Tasks:
1. Define convert_temperature(value, from_unit, to_unit="C")
2. Support units: C, F, K (case-insensitive)
3. Return None for unknown units
4. Convert a list of readings to target units
5. Print a formatted report

Inputs:
readings = [
    ("Morning", 68, "F", "C"),
    ("Noon", 295.15, "K", "C"),
    ("Evening", 22, "C", "F"),
    ("Night", 60, "F", "K")
]

Expected Output:
Morning: 68°F = 20.0°C
Noon: 295.15K = 22.0°C
Evening: 22°C = 71.6°F
Night: 60°F = 288.7K

Hints:
- Normalize units using .upper()
- Convert from source to Celsius, then to target
- Use default parameter for to_unit

Rubric:
- Correct unit conversions: 40%
- Proper default args: 20%
- Return None for unknown units: 20%
- Output formatting: 20%
"""

# Input data
readings = [
    ("Morning", 68, "F", "C"),
    ("Noon", 295.15, "K", "C"),
    ("Evening", 22, "C", "F"),
    ("Night", 60, "F", "K")
]

# Your code here

