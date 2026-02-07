"""
Solution: Beginner Assignment 3 - BMI Calculator
"""

# Input data
users = [
    ("User 1", 70, 1.75),
    ("User 2", 85, 1.80)
]

# Function definitions
def calculate_bmi(weight_kg, height_m):
    """Calculate BMI from weight and height"""
    return weight_kg / (height_m ** 2)

def get_bmi_category(bmi):
    """Return BMI category based on value"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

# Process each user
for name, weight, height in users:
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    print(f"{name}: BMI = {bmi:.2f} ({category})")
