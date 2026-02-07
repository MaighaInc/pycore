"""
Solution: Advanced Assignment 5 - Grade Calculator
"""

# Input data
students = [
    ("Maya", [92, 85, 88, 90], [0.3, 0.2, 0.2, 0.3]),
    ("Ethan", [75, 80, 70, 68], [0.4, 0.2, 0.2, 0.2]),
    ("Zoe", [98, 95, 100, 92], [0.2, 0.3, 0.3, 0.2])
]

# Helpers
def drop_lowest(scores):
    scores = scores[:]  # copy
    scores.remove(min(scores))
    return scores

def apply_curve(scores, curve_points):
    return [min(100, s + curve_points) for s in scores]

def calculate_weighted_average(scores, weights):
    return sum(s * w for s, w in zip(scores, weights))

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

def calculate_final(scores, weights=None, drop=False, curve=0):
    if drop:
        scores = drop_lowest(scores)
        if weights is not None:
            weights = weights[:]
            weights.pop(weights.index(min(weights)))

    if curve:
        scores = apply_curve(scores, curve)

    if weights is None:
        return sum(scores) / len(scores)

    return calculate_weighted_average(scores, weights)

# Report
for name, scores, weights in students:
    final_score = calculate_final(scores, weights, drop=True, curve=2)
    grade = get_letter_grade(final_score)
    print(f"{name}: Final {final_score:.1f} = Grade {grade}")
