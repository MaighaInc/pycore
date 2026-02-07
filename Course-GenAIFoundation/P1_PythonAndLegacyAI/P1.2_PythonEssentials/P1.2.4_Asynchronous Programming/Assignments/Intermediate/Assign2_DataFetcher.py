"""
Intermediate Assignment 2: Async Data Fetcher

Scenario:
Limit concurrent fetches and add timeouts.

Objective:
Use semaphores and asyncio.wait_for.

Tasks:
1. Create async fetch_data(url, delay)
2. Use asyncio.Semaphore to limit concurrency to 2
3. Use asyncio.wait_for with timeout=1.5
4. Print results and timeouts

Inputs:
requests = [
    ("/users", 0.8),
    ("/orders", 1.2),
    ("/products", 0.5),
    ("/reports", 2.0)
]

Expected Output (sample):
Fetched /users
Fetched /orders
Fetched /products
Timeout /reports

Hints:
- Use async with semaphore
- Wrap fetch with asyncio.wait_for

Rubric:
- Correct concurrency limit: 40%
- Proper timeout handling: 40%
- Output formatting: 20%
"""

import asyncio

# Input data
requests = [
    ("/users", 0.8),
    ("/orders", 1.2),
    ("/products", 0.5),
    ("/reports", 2.0)
]

# Your code here

