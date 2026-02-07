"""
Advanced Assignment 2: User Input Validator

Scenario:
A registration system validates user records and raises structured
validation errors.

Objective:
Build a validation layer with custom exceptions and error aggregation.

Tasks:
1. Create ValidationError exception with message and field
2. Create validators:
   - validate_age(value)
   - validate_email(value)
   - validate_score(value)
3. Create validate_user(user) that collects errors and returns list
4. Print a summary report with error counts

Inputs:
users = [
    {"name": "Ava", "age": "25", "email": "ava@mail.com", "score": "88.5"},
    {"name": "Liam", "age": "-2", "email": "liam.mail.com", "score": "90"},
    {"name": "Noah", "age": "abc", "email": "noah@mail", "score": "105"}
]

Expected Output (sample):
Ava: Valid
Liam: age -> out of range, email -> invalid
Noah: age -> not a number, email -> invalid, score -> out of range

Hints:
- Raise ValidationError inside validators
- Catch and collect errors in validate_user
- Track error counts per field

Rubric:
- Proper custom error usage: 30%
- Correct validation logic: 40%
- Clear reporting: 30%
"""

# Test data
users = [
    {"name": "Ava", "age": "25", "email": "ava@mail.com", "score": "88.5"},
    {"name": "Liam", "age": "-2", "email": "liam.mail.com", "score": "90"},
    {"name": "Noah", "age": "abc", "email": "noah@mail", "score": "105"}
]

# Your code here

