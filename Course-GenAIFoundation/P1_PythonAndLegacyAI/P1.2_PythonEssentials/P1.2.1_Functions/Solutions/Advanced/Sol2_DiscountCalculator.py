"""
Solution: Advanced Assignment 2 - Discount Calculator
"""

# Input data
cart = [
    ("Shoes", 120, ["PCT:15", "COUPON:SAVE10"]),
    ("Jacket", 200, ["PCT:20"]),
    ("Socks", 25, ["COUPON:SAVE25"]),
    ("Hat", 40, ["PCT:5", "FIXED:3"])
]

# Rule factories
def percent_off(pct):
    return lambda price: price * (1 - pct / 100)

def fixed_off(amount):
    return lambda price: max(0, price - amount)

def coupon(code):
    coupons = {"SAVE10": 10, "SAVE25": 25}
    pct = coupons.get(code, 0)
    return lambda price: price * (1 - pct / 100)

def apply_rules(price, *rules):
    for rule in rules:
        price = rule(price)
    return price

def parse_rules(rule_strings):
    rules = []
    for rule in rule_strings:
        kind, value = rule.split(":", 1)
        if kind == "PCT":
            rules.append(percent_off(float(value)))
        elif kind == "FIXED":
            rules.append(fixed_off(float(value)))
        elif kind == "COUPON":
            rules.append(coupon(value))
    return rules

# Build receipt
total = 0
for name, price, rule_strings in cart:
    rules = parse_rules(rule_strings)
    final = apply_rules(price, *rules)
    total += final
    print(f"{name}: ${price:.2f} -> ${final:.2f}")

print(f"\nTotal: ${total:.2f}")
