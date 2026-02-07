"""
Advanced Assignment 4: Password Strength Checker

Scenario:
Your security team wants a configurable password policy with reporting.

Objective:
Create a rule-based password evaluator using higher-order functions.

Tasks:
1. Create rule functions that return True/False:
   - min_length(n)
   - has_digit()
   - has_upper()
   - has_lower()
   - has_special(chars)
2. Create evaluate(password, rules) that returns score and failed rules
3. Create a decorator report_results(func) that formats output
4. Run evaluation for all passwords and print report

Inputs:
passwords = ["hello123", "Password1", "Str0ng!Pass", "short", "NoDigitsHere"]

Expected Output (sample):
Password: hello123 | score 3/5 | failed: has_upper, has_special
Password: Password1 | score 4/5 | failed: has_special
Password: Str0ng!Pass | score 5/5 | failed: none
...

Hints:
- Each rule can be a lambda that captures parameters
- Return both score and failed rule names
- Use decorator to standardize printing

Rubric:
- Correct rule functions: 30%
- Proper evaluation logic: 30%
- Decorator usage: 20%
- Output formatting: 20%
"""

# Input data
passwords = ["hello123", "Password1", "Str0ng!Pass", "short", "NoDigitsHere"]

# Your code here

