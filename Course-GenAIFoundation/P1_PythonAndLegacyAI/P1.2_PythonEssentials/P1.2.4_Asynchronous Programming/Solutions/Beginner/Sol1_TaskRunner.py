"""
Solution: Beginner Assignment 1 - Async Task Runner
"""

import asyncio

# Input data
tasks = [
    ("Task A", 1),
    ("Task B", 2),
    ("Task C", 1)
]

async def wait_and_print(name, seconds):
    print(f"Starting {name}")
    await asyncio.sleep(seconds)
    print(f"Finished {name}")

async def main():
    for name, seconds in tasks:
        await wait_and_print(name, seconds)

asyncio.run(main())
