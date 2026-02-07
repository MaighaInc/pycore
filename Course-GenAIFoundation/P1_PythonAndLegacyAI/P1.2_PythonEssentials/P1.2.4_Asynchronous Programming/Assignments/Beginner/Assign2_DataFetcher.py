"""
Beginner Assignment 2: Async Data Fetcher

Scenario:
Simulate fetching data from multiple URLs asynchronously.

Objective:
Use asyncio.gather to run tasks concurrently.

Tasks:
1. Create async function fetch_data(url)
2. Simulate network delay using asyncio.sleep
3. Return a string with the result
4. Use asyncio.gather to fetch all URLs

Inputs:
urls = ["/users", "/orders", "/products"]

Expected Output:
Fetched /users
Fetched /orders
Fetched /products

Hints:
- Use asyncio.gather(*tasks)
- Use random delays for realism

Rubric:
- Correct async function: 35%
- Correct concurrency with gather: 45%
- Output formatting: 20%
"""

import asyncio
import random

# Input data
urls = ["/users", "/orders", "/products"]

# Your code here

