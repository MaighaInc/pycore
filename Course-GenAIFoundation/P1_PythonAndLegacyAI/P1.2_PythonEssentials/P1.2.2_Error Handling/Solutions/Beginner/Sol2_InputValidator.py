"""
Solution: Beginner Assignment 2 - User Input Validator
"""

# Test inputs
test_inputs = ["25", "abc", "150", "-5"]

def validate_age(age_input):
    try:
        age = int(age_input)
        if 0 <= age <= 120:
            return "Valid age"
        return "Error: Age must be between 0 and 120"
    except ValueError:
        return "Error: Invalid number format"

# Process inputs
for value in test_inputs:
    print(f"Input: {value} - {validate_age(value)}")
