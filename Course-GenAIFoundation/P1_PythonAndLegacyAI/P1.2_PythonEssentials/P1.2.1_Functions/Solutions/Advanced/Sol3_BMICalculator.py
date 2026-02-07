"""
Solution: Advanced Assignment 3 - BMI Calculator
"""

# Input data
users = [
    {"name": "Ava", "weight": 70, "height": 1.75, "unit": "metric"},
    {"name": "Liam", "weight": 180, "height": 70, "unit": "imperial"},
    {"name": "Noah", "weight": 95, "height": 1.82, "unit": "metric"},
    {"name": "Mia", "weight": 50, "height": 1.62, "unit": "metric"}
]

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

def to_bmi_record(user):
    if user["unit"] == "metric":
        bmi = bmi_metric(user["weight"], user["height"])
    else:
        bmi = bmi_imperial(user["weight"], user["height"])
    return {
        "name": user["name"],
        "bmi": round(bmi, 2),
        "category": get_bmi_category(bmi)
    }

def summarize_bmi(records, *, group_by_category=True):
    summary = {}
    if not group_by_category:
        return summary

    for record in records:
        cat = record["category"]
        summary.setdefault(cat, []).append(record["bmi"])

    return {cat: round(sum(values) / len(values), 2) for cat, values in summary.items()}

# Build report
bmi_records = [to_bmi_record(u) for u in users]

print("BMI Report")
print("=" * 10)
for record in bmi_records:
    print(f"{record['name']}: {record['bmi']:.2f} ({record['category']})")

print("\nCategory Averages:")
for category, avg in summarize_bmi(bmi_records).items():
    print(f"{category}: {avg:.2f}")
