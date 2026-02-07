"""
Solution: Advanced Assignment 4 - Password Strength Checker
"""

from functools import wraps

# Input data
passwords = ["hello123", "Password1", "Str0ng!Pass", "short", "NoDigitsHere"]

# Rule factories
def min_length(n):
    return (f"min_length({n})", lambda pwd: len(pwd) >= n)

def has_digit():
    return ("has_digit", lambda pwd: any(ch.isdigit() for ch in pwd))

def has_upper():
    return ("has_upper", lambda pwd: any(ch.isupper() for ch in pwd))

def has_lower():
    return ("has_lower", lambda pwd: any(ch.islower() for ch in pwd))

def has_special(chars="!@#$%^&*"):
    return ("has_special", lambda pwd: any(ch in chars for ch in pwd))

# Decorator for reporting
def report_results(func):
    @wraps(func)
    def wrapper(password, rules):
        score, failed = func(password, rules)
        failed_text = ", ".join(failed) if failed else "none"
        print(f"Password: {password} | score {score}/{len(rules)} | failed: {failed_text}")
        return score, failed
    return wrapper

@report_results
def evaluate(password, rules):
    failed = []
    score = 0
    for name, rule_fn in rules:
        if rule_fn(password):
            score += 1
        else:
            failed.append(name)
    return score, failed

rules = [
    min_length(8),
    has_digit(),
    has_upper(),
    has_lower(),
    has_special()
]

for pwd in passwords:
    evaluate(pwd, rules)
