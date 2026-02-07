"""
Intermediate Assignment 2: Discount Calculator

Scenario:
A store applies discounts based on item category and optional coupons.
Build reusable functions to compute final prices and totals.

Objective:
Use default arguments and helper functions to calculate discounts.

Tasks:
1. Define calculate_discount(price, discount_percent=0)
2. Define apply_coupon(price, coupon_code=None)
   - "SAVE10" -> extra 10% off
   - "SAVE25" -> extra 25% off
   - None/unknown -> no change
3. Define final_price(price, discount_percent=0, coupon_code=None)
4. Process the cart and print a receipt

Inputs:
cart = [
    ("Shoes", 120, 15, "SAVE10"),
    ("Jacket", 200, 20, None),
    ("Socks", 25, 0, "SAVE25"),
    ("Hat", 40, 5, "SAVE10")
]

Expected Output:
Shoes: $120.00 -> $91.80
Jacket: $200.00 -> $160.00
Socks: $25.00 -> $18.75
Hat: $40.00 -> $34.20

Total: $304.75

Hints:
- Apply discount first, then coupon
- Use default parameters for flexibility
- Use helper functions to keep code clean

Rubric:
- Correct discount calculation: 35%
- Correct coupon application: 25%
- Clean function decomposition: 20%
- Output formatting: 20%
"""

# Input data
cart = [
    ("Shoes", 120, 15, "SAVE10"),
    ("Jacket", 200, 20, None),
    ("Socks", 25, 0, "SAVE25"),
    ("Hat", 40, 5, "SAVE10")
]

# Your code here

