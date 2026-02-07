"""
Solution: Beginner Assignment 4 - Password Strength Checker
"""

# Input data
passwords = ["hello123", "Password1", "short"]

# Function definition
def check_password_strength(password):
    """Check if password meets security criteria"""
    # Check length
    has_length = len(password) >= 8
    
    # Check for digit
    has_digit = any(char.isdigit() for char in password)
    
    # Check for uppercase
    has_upper = any(char.isupper() for char in password)
    
    # Return strength based on all criteria
    if has_length and has_digit and has_upper:
        return "Strong"
    else:
        return "Weak"

# Test each password
for pwd in passwords:
    strength = check_password_strength(pwd)
    print(f"Password: {pwd} - {strength}")
