"""
Solution: Intermediate Assignment 1 - Async Task Runner
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
    loop = asyncio.get_event_loop()
    start = loop.time()
    await asyncio.gather(*(wait_and_print(n, s) for n, s in tasks))
    duration = loop.time() - start
    print(f"Total runtime: {duration:.2f}s")

asyncio.run(main())
