"""
Beginner Assignment 4: Password Strength Checker

Scenario:
A website needs to check if user passwords meet minimum security requirements.

Objective:
Create a function that evaluates password strength based on simple criteria.

Tasks:
1. Define a function check_password_strength(password)
2. Check if password meets these criteria:
   - At least 8 characters long
   - Contains at least one digit
   - Contains at least one uppercase letter
3. Return "Strong" if all criteria met, otherwise "Weak"
4. Test with provided passwords

Inputs:
- "hello123" - Weak (no uppercase)
- "Password1" - Strong (meets all criteria)
- "short" - Weak (too short, no digit, no uppercase)

Expected Output:
Password: hello123 - Weak
Password: Password1 - Strong
Password: short - Weak

Hints:
- Use len() for length check
- Use .isdigit() to check for digits
- Use .isupper() to check for uppercase
- Use any() with generator expression

Rubric:
- Correct length check: 25%
- Correct digit check: 25%
- Correct uppercase check: 25%
- Proper output: 25%
"""

# Input data
passwords = ["hello123", "Password1", "short"]

# Your code here

