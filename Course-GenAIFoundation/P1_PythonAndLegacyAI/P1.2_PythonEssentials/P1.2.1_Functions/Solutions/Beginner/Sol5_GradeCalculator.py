"""
Solution: Beginner Assignment 5 - Grade Calculator
"""

# Input data
students = [
    ("Student 1", 95),
    ("Student 2", 87),
    ("Student 3", 72),
    ("Student 4", 65),
    ("Student 5", 58)
]

# Function definition
def get_letter_grade(score):
    """Convert numerical score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Process each student
for name, score in students:
    grade = get_letter_grade(score)
    print(f"{name}: Score {score} = Grade {grade}")
