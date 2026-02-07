"""
Solution: Beginner Assignment 3 - Async Queue Processor
"""

import asyncio

# Input data
items = ["file1", "file2", "file3"]

async def process_item(item):
    print(f"Processing {item}")
    await asyncio.sleep(0.5)
    print(f"Done {item}")

async def process_queue(items):
    for item in items:
        await process_item(item)

asyncio.run(process_queue(items))
