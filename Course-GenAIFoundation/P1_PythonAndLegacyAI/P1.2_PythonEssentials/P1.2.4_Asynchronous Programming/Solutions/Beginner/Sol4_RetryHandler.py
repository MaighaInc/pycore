"""
Solution: Beginner Assignment 4 - Async Retry Handler
"""

import asyncio
import random

async def unreliable_task():
    await asyncio.sleep(0.2)
    if random.choice([True, False]):
        raise RuntimeError("Temporary failure")
    return "Success"

async def run_with_retries(max_retries):
    for attempt in range(1, max_retries + 1):
        try:
            result = await unreliable_task()
            print(f"Success on attempt {attempt}")
            return result
        except Exception:
            print(f"Attempt {attempt} failed")
    print("All retries exhausted")

asyncio.run(run_with_retries(3))
