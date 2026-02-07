"""
Beginner Assignment 2: User Input Validator

Scenario:
Validate user input for age registration, handling invalid integers.

Objective:
Use try-except to handle ValueError when converting strings to integers.

Tasks:
1. Create a function validate_age(age_input)
2. Try to convert input to integer
3. Check if age is between 0 and 120
4. Return valid age or error message
5. Test with various inputs

Inputs:
- "25" (valid)
- "abc" (not a number)
- "150" (out of range)
- "-5" (negative)

Expected Output:
Input: 25 - Valid age
Input: abc - Error: Invalid number format
Input: 150 - Error: Age must be between 0 and 120
Input: -5 - Error: Age must be between 0 and 120

Hints:
- Use try-except ValueError for conversion
- Use if statements for range validation
- Return different messages for different errors

Rubric:
- Correct ValueError handling: 40%
- Proper range validation: 30%
- Clear error messages: 30%
"""

# Test inputs
test_inputs = ["25", "abc", "150", "-5"]

# Your code here

