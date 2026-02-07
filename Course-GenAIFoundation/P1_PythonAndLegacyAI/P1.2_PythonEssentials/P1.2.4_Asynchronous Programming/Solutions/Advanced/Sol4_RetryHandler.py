"""
Solution: Advanced Assignment 4 - Async Retry Handler
"""

import asyncio
import random

async def unreliable_task():
    await asyncio.sleep(0.2)
    if random.choice([True, False]):
        raise RuntimeError("Temporary failure")
    return "Success"

async def run_with_retries(max_retries, base_delay, timeout):
    async def _runner():
        for attempt in range(1, max_retries + 1):
            try:
                await unreliable_task()
                print(f"Success on attempt {attempt}")
                return
            except Exception:
                jitter = random.uniform(0, 0.2)
                delay = base_delay * (2 ** (attempt - 1)) + jitter
                print(f"Attempt {attempt} failed (retry in {delay:.2f}s)")
                await asyncio.sleep(delay)
        print("All retries exhausted")

    try:
        await asyncio.wait_for(_runner(), timeout=timeout)
    except asyncio.TimeoutError:
        print("Retry operation timed out")

asyncio.run(run_with_retries(5, 0.3, 3.0))
