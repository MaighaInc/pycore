"""
Advanced Assignment 1: Temperature Converter

Scenario:
You are building a conversion service with logging, caching, and reusable
converter factories.

Objective:
Create higher-order functions and decorators to build a robust converter.

Tasks:
1. Create a decorator log_conversion(func) that logs input and output
2. Create a decorator cache_results(func) that caches conversions by arguments
3. Create a function make_converter(from_unit, to_unit) that returns a function
4. Support C, F, K conversions
5. Process a batch of readings using factory-generated converters

Inputs:
readings = [
    ("Morning", 68, "F", "C"),
    ("Noon", 295.15, "K", "C"),
    ("Evening", 22, "C", "F"),
    ("Night", 60, "F", "K"),
    ("Repeat", 68, "F", "C")
]

Expected Output (sample):
[LOG] F->C 68 => 20.0
[LOG] K->C 295.15 => 22.0
[LOG] C->F 22 => 71.6
[LOG] F->K 60 => 288.7
[LOG] F->C 68 => 20.0 (cached)

Hints:
- Use functools.wraps in decorators
- Cache key can be args tuple
- Factory returns function that takes a value

Rubric:
- Correct converter factory: 30%
- Proper caching decorator: 25%
- Logging decorator: 20%
- Batch processing: 25%
"""

# Input data
readings = [
    ("Morning", 68, "F", "C"),
    ("Noon", 295.15, "K", "C"),
    ("Evening", 22, "C", "F"),
    ("Night", 60, "F", "K"),
    ("Repeat", 68, "F", "C")
]

# Your code here

