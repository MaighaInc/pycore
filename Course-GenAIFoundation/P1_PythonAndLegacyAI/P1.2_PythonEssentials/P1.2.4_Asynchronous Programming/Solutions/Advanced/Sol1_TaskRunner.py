"""
Solution: Advanced Assignment 1 - Async Task Runner
"""

import asyncio

# Input data
tasks = [
    ("Task A", 1),
    ("Task B", 3),
    ("Task C", 2)
]

async def wait_and_print(name, seconds):
    try:
        await asyncio.sleep(seconds)
        print(f"Finished {name}")
    except asyncio.CancelledError:
        print(f"Cancelled {name}")
        raise

async def main():
    running = [asyncio.create_task(wait_and_print(n, s)) for n, s in tasks]
    done, pending = await asyncio.wait(running, timeout=2.0)

    for task in pending:
        task.cancel()

    if pending:
        await asyncio.gather(*pending, return_exceptions=True)

asyncio.run(main())
