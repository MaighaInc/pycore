"""
Advanced Assignment 2: Discount Calculator

Scenario:
A pricing engine supports multiple discount strategies and rule chaining.

Objective:
Use higher-order functions to compose discount rules.

Tasks:
1. Create discount rules as functions:
   - percent_off(pct)
   - fixed_off(amount)
   - coupon(code)
2. Create apply_rules(price, *rules) that applies rules in order
3. Create build_receipt(cart, rule_builder) where rule_builder returns rule list
4. Print item-level and total results

Inputs:
cart = [
    ("Shoes", 120, ["PCT:15", "COUPON:SAVE10"]),
    ("Jacket", 200, ["PCT:20"]),
    ("Socks", 25, ["COUPON:SAVE25"]),
    ("Hat", 40, ["PCT:5", "FIXED:3"])
]

Expected Output (sample):
Shoes: $120.00 -> $91.80
Jacket: $200.00 -> $160.00
Socks: $25.00 -> $18.75
Hat: $40.00 -> $35.00

Total: $305.55

Hints:
- Rule functions should return a new price
- Use lambdas to create rule functions
- Parse rule strings into rule functions

Rubric:
- Correct rule functions: 30%
- Proper rule chaining: 30%
- Correct parsing logic: 20%
- Output formatting: 20%
"""

# Input data
cart = [
    ("Shoes", 120, ["PCT:15", "COUPON:SAVE10"]),
    ("Jacket", 200, ["PCT:20"]),
    ("Socks", 25, ["COUPON:SAVE25"]),
    ("Hat", 40, ["PCT:5", "FIXED:3"])
]

# Your code here

