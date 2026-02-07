"""
Solution: Intermediate Assignment 5 - Grade Calculator
"""

# Input data
students = [
    ("Maya", [92, 85, 88], [0.4, 0.3, 0.3]),
    ("Ethan", [75, 80, 70], [0.5, 0.2, 0.3]),
    ("Zoe", [98, 95, 100], [0.3, 0.3, 0.4])
]

# Function definitions
def calculate_weighted_average(scores, weights):
    total = 0
    for score, weight in zip(scores, weights):
        total += score * weight
    return total

def get_letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

# Process students
for name, scores, weights in students:
    final_score = calculate_weighted_average(scores, weights)
    grade = get_letter_grade(final_score)
    print(f"{name}: Final {final_score:.1f} = Grade {grade}")
