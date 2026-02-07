"""
Solution: Intermediate Assignment 4 - Async Retry Handler
"""

import asyncio
import random

async def unreliable_task():
    await asyncio.sleep(0.2)
    if random.choice([True, False]):
        raise RuntimeError("Temporary failure")
    return "Success"

async def run_with_retries(max_retries, base_delay):
    for attempt in range(1, max_retries + 1):
        try:
            await unreliable_task()
            print(f"Success on attempt {attempt}")
            return
        except Exception:
            delay = base_delay * (2 ** (attempt - 1))
            print(f"Attempt {attempt} failed (retry in {delay:.1f}s)")
            await asyncio.sleep(delay)
    print("All retries exhausted")

asyncio.run(run_with_retries(4, 0.5))
