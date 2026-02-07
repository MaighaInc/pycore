"""
Solution: Advanced Assignment 2 - User Input Validator
"""

# Test data
users = [
    {"name": "Ava", "age": "25", "email": "ava@mail.com", "score": "88.5"},
    {"name": "Liam", "age": "-2", "email": "liam.mail.com", "score": "90"},
    {"name": "Noah", "age": "abc", "email": "noah@mail", "score": "105"}
]

class ValidationError(Exception):
    def __init__(self, field, message):
        super().__init__(message)
        self.field = field
        self.message = message

# Validators
def validate_age(value):
    try:
        age = int(value)
    except ValueError:
        raise ValidationError("age", "not a number")
    if not (0 <= age <= 120):
        raise ValidationError("age", "out of range")

def validate_email(value):
    if "@" not in value or "." not in value:
        raise ValidationError("email", "invalid")

def validate_score(value):
    try:
        score = float(value)
    except ValueError:
        raise ValidationError("score", "not a number")
    if not (0 <= score <= 100):
        raise ValidationError("score", "out of range")

def validate_user(user):
    errors = []
    for validator in (validate_age, validate_email, validate_score):
        try:
            validator(user.get(validator.__name__.replace("validate_", "")))
        except ValidationError as e:
            errors.append((e.field, e.message))
    return errors

# Process users
for user in users:
    errors = validate_user(user)
    if not errors:
        print(f"{user['name']}: Valid")
    else:
        error_text = ", ".join(f"{field} -> {msg}" for field, msg in errors)
        print(f"{user['name']}: {error_text}")
