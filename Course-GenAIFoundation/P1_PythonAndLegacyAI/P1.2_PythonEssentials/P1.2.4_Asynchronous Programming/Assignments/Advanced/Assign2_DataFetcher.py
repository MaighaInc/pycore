"""
Advanced Assignment 2: Async Data Fetcher

Scenario:
Fetch data with concurrency limits, timeouts, and error collection.

Objective:
Use semaphores and gather with return_exceptions.

Tasks:
1. Create fetch_data(url, delay) that may raise TimeoutError
2. Limit concurrency to 3 using Semaphore
3. Use asyncio.wait_for with timeout=1.5
4. Collect successes and failures
5. Print a summary

Inputs:
requests = [
    ("/users", 0.8),
    ("/orders", 1.2),
    ("/products", 0.5),
    ("/reports", 2.0),
    ("/stats", 1.8)
]

Expected Output (sample):
Success: /users
Success: /orders
Timeout: /reports
Timeout: /stats

Hints:
- Use return_exceptions=True
- Distinguish TimeoutError vs success

Rubric:
- Correct concurrency: 30%
- Correct timeout handling: 40%
- Summary reporting: 30%
"""

import asyncio

# Input data
requests = [
    ("/users", 0.8),
    ("/orders", 1.2),
    ("/products", 0.5),
    ("/reports", 2.0),
    ("/stats", 1.8)
]

# Your code here

