"""
Beginner Assignment 4: Async Retry Handler

Scenario:
Retry a failing async operation a limited number of times.

Objective:
Use loops with async functions and handle exceptions.

Tasks:
1. Create async function unreliable_task() that fails randomly
2. Create async function run_with_retries(max_retries)
3. Retry on exception and print attempts
4. Stop when success or retries exhausted

Inputs:
max_retries = 3

Expected Output (sample):
Attempt 1 failed
Attempt 2 failed
Success on attempt 3

Hints:
- Use try/except inside async function
- Use random.choice to simulate failure

Rubric:
- Correct retry logic: 50%
- Proper async handling: 30%
- Output formatting: 20%
"""

import asyncio
import random

# Your code here

