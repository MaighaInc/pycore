"""
Advanced Assignment 4: Async Retry Handler

Scenario:
Retry an async task with exponential backoff, jitter, and global timeout.

Objective:
Implement robust retry behavior.

Tasks:
1. Create async unreliable_task() that fails randomly
2. Create async run_with_retries(max_retries, base_delay, timeout)
3. Add jitter: random.uniform(0, 0.2)
4. Use asyncio.wait_for to enforce total timeout
5. Print attempt outcomes

Inputs:
max_retries = 5, base_delay = 0.3, timeout = 3.0

Expected Output (sample):
Attempt 1 failed (retry in 0.31s)
Attempt 2 failed (retry in 0.65s)
Success on attempt 3

Hints:
- Track elapsed time
- Raise if total timeout exceeded

Rubric:
- Correct retry and backoff: 40%
- Correct timeout logic: 40%
- Output formatting: 20%
"""

import asyncio
import random

# Your code here

