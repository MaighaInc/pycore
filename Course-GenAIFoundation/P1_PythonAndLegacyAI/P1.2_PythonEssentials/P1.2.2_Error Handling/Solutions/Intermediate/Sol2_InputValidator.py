"""
Solution: Intermediate Assignment 2 - User Input Validator
"""

# Test data
users = [
    {"name": "Ava", "age": "25", "email": "ava@mail.com", "score": "88.5"},
    {"name": "Liam", "age": "-2", "email": "liam.mail.com", "score": "90"},
    {"name": "Noah", "age": "abc", "email": "noah@mail", "score": "105"}
]

def validate_user(user):
    errors = []

    # Validate age
    try:
        age = int(user["age"])
        if not (0 <= age <= 120):
            errors.append("Age out of range")
    except ValueError:
        errors.append("Age not a number")

    # Validate email
    email = user.get("email", "")
    if "@" not in email or "." not in email:
        errors.append("Email invalid")

    # Validate score
    try:
        score = float(user["score"])
        if not (0 <= score <= 100):
            errors.append("Score out of range")
    except ValueError:
        errors.append("Score not a number")

    return errors

# Process users
for user in users:
    errors = validate_user(user)
    if not errors:
        print(f"{user['name']}: Valid")
    else:
        print(f"{user['name']}: Errors -> {', '.join(errors)}")
