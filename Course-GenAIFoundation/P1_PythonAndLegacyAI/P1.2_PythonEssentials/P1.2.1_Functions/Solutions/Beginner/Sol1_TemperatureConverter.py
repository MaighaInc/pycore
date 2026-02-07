"""
Solution: Beginner Assignment 1 - Temperature Converter
"""

# Input data
temp_c = 25
temp_f = 77

# Function definitions
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

# Test conversions
result_f = celsius_to_fahrenheit(temp_c)
result_c = fahrenheit_to_celsius(temp_f)

# Display results
print(f"{temp_c}°C = {result_f}°F")
print(f"{temp_f}°F = {result_c}°C")
