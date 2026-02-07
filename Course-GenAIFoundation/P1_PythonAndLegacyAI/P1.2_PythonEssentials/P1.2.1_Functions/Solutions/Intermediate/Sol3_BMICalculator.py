"""
Solution: Intermediate Assignment 3 - BMI Calculator
"""

# Input data
users = [
    {"name": "Ava", "weight": 70, "height": 1.75, "unit": "metric"},
    {"name": "Liam", "weight": 180, "height": 70, "unit": "imperial"},
    {"name": "Noah", "weight": 95, "height": 1.82, "unit": "metric"}
]

# Function definitions
def bmi_metric(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_imperial(weight_lb, height_in):
    return (weight_lb / (height_in ** 2)) * 703

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25.0:
        return "Normal weight"
    if bmi < 30.0:
        return "Overweight"
    return "Obese"

# Process users
for user in users:
    if user["unit"] == "metric":
        bmi = bmi_metric(user["weight"], user["height"])
    else:
        bmi = bmi_imperial(user["weight"], user["height"])

    category = get_bmi_category(bmi)
    print(f"{user['name']}: BMI = {bmi:.2f} ({category})")
