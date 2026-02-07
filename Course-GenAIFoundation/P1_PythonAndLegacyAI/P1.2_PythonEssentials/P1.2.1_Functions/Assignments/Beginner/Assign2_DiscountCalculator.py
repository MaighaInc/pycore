"""
Beginner Assignment 2: Discount Calculator

Scenario:
A retail store needs a function to calculate the final price after applying
a discount percentage.

Objective:
Create a function that calculates the discounted price.

Tasks:
1. Define a function calculate_discount(price, discount_percent) 
2. The function should calculate and return the final price after discount
3. Test the function with multiple product prices
4. Print each result showing original price, discount, and final price

Inputs:
- Product A: price = 100, discount = 20%
- Product B: price = 250, discount = 15%
- Product C: price = 50, discount = 10%

Expected Output:
Product A: $100.00 - 20% discount = $80.00
Product B: $250.00 - 15% discount = $212.50
Product C: $50.00 - 10% discount = $45.00

Hints:
- discount_amount = price * (discount_percent / 100)
- final_price = price - discount_amount
- Use .2f for 2 decimal places

Rubric:
- Correct function definition: 40%
- Correct calculation logic: 40%
- Proper function calls and output: 20%
"""

# Input data
products = [
    ("Product A", 100, 20),
    ("Product B", 250, 15),
    ("Product C", 50, 10)
]

# Your code here

