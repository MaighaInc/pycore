"""
Intermediate Assignment 2: User Input Validator

Scenario:
Validate user registration data with multiple fields and error reporting.

Objective:
Use exceptions to validate multiple input fields safely.

Tasks:
1. Create validate_user(user) that checks:
   - age (int, 0-120)
   - email (must contain '@' and '.')
   - score (float between 0 and 100)
2. Return a list of errors (empty if valid)
3. Process the user list and print validation report

Inputs:
users = [
    {"name": "Ava", "age": "25", "email": "ava@mail.com", "score": "88.5"},
    {"name": "Liam", "age": "-2", "email": "liam.mail.com", "score": "90"},
    {"name": "Noah", "age": "abc", "email": "noah@mail", "score": "105"}
]

Expected Output:
Ava: Valid
Liam: Errors -> Age out of range, Email invalid
Noah: Errors -> Age not a number, Email invalid, Score out of range

Hints:
- Use try/except ValueError when converting age and score
- Validate email with basic rules (contains '@' and '.')

Rubric:
- Correct field validation: 40%
- Proper error collection: 30%
- Clear reporting: 30%
"""

# Test data
users = [
    {"name": "Ava", "age": "25", "email": "ava@mail.com", "score": "88.5"},
    {"name": "Liam", "age": "-2", "email": "liam.mail.com", "score": "90"},
    {"name": "Noah", "age": "abc", "email": "noah@mail", "score": "105"}
]

# Your code here

