"""
Solution: Intermediate Assignment 4 - Password Strength Checker
"""

# Input data
passwords = ["hello123", "Password1", "Str0ng!Pass", "short", "NoDigitsHere"]

# Function definitions
def score_password(password):
    score = 0
    if len(password) >= 8:
        score += 2
    if len(password) >= 12:
        score += 2
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch.islower() for ch in password):
        score += 1
    if any(ch in "!@#$%^&*" for ch in password):
        score += 1
    return score

def strength_label(score):
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Medium"
    return "Strong"

# Evaluate passwords
for pwd in passwords:
    score = score_password(pwd)
    label = strength_label(score)
    print(f"{pwd} -> score {score} ({label})")
