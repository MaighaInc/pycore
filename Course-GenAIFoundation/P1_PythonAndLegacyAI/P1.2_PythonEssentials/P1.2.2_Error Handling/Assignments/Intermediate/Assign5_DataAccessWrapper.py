"""
Intermediate Assignment 5: Data Access Wrapper

Scenario:
Access nested user records and compute profile completeness scores.

Objective:
Use robust exception handling for nested dictionary access.

Tasks:
1. Create get_profile_score(user, required_fields)
   - Return percentage of required fields present
2. Handle KeyError for missing fields
3. Handle TypeError for invalid user data
4. Always print "Profile check completed" in finally block
5. Test with provided user records

Inputs:
users = [
    {"name": "Alice", "age": 25, "email": "alice@test.com"},
    {"name": "Bob", "age": 30},
    None,
    {"name": "Carol", "email": "carol@test.com"}
]

required = ["name", "age", "email"]

Expected Output:
User 0 -> 100.0% complete
User 1 -> 66.7% complete
User 2 -> Error: Invalid user data
User 3 -> 66.7% complete

Hints:
- Count how many required fields exist
- Percentage = (found / total) * 100
- Use try/except/finally

Rubric:
- Correct score calculation: 35%
- Proper exception handling: 35%
- Finally usage: 20%
- Output formatting: 10%
"""

# Test data
users = [
    {"name": "Alice", "age": 25, "email": "alice@test.com"},
    {"name": "Bob", "age": 30},
    None,
    {"name": "Carol", "email": "carol@test.com"}
]

required = ["name", "age", "email"]

# Your code here

