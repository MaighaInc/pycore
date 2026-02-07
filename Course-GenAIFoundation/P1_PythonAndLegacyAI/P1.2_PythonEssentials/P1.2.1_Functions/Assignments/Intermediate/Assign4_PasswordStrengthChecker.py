"""
Intermediate Assignment 4: Password Strength Checker

Scenario:
Improve password checks by scoring multiple criteria instead of only
pass/fail.

Objective:
Create functions that score and label password strength.

Tasks:
1. Define score_password(password) returning an integer score
2. Add points:
   - +2 for length >= 8
   - +2 for length >= 12
   - +1 if contains digit
   - +1 if contains uppercase
   - +1 if contains lowercase
   - +1 if contains special character (!@#$%^&*)
3. Define strength_label(score)
   - 0-2: Weak
   - 3-4: Medium
   - 5-7: Strong
4. Evaluate all passwords and print score + label

Inputs:
passwords = ["hello123", "Password1", "Str0ng!Pass", "short", "NoDigitsHere"]

Expected Output:
hello123 -> score 3 (Medium)
Password1 -> score 5 (Strong)
Str0ng!Pass -> score 7 (Strong)
short -> score 1 (Weak)
NoDigitsHere -> score 3 (Medium)

Hints:
- Use any() with generator expressions
- Special characters set: "!@#$%^&*"
- Keep scoring logic in a dedicated function

Rubric:
- Correct scoring logic: 40%
- Correct label mapping: 30%
- Clean function structure: 20%
- Output formatting: 10%
"""

# Input data
passwords = ["hello123", "Password1", "Str0ng!Pass", "short", "NoDigitsHere"]

# Your code here

