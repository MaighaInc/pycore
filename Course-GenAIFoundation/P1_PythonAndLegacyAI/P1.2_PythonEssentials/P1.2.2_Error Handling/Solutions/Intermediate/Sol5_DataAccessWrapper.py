"""
Solution: Intermediate Assignment 5 - Data Access Wrapper
"""

# Test data
users = [
    {"name": "Alice", "age": 25, "email": "alice@test.com"},
    {"name": "Bob", "age": 30},
    None,
    {"name": "Carol", "email": "carol@test.com"}
]

required = ["name", "age", "email"]

def get_profile_score(user, required_fields):
    try:
        if user is None:
            raise TypeError("Invalid user data")
        
        found = sum(1 for field in required_fields if field in user)
        return (found / len(required_fields)) * 100
    except TypeError:
        return "Error: Invalid user data"
    finally:
        print("Profile check completed")

# Process users
for i, user in enumerate(users):
    result = get_profile_score(user, required)
    if isinstance(result, str):
        print(f"User {i} -> {result}")
    else:
        print(f"User {i} -> {result:.1f}% complete")
