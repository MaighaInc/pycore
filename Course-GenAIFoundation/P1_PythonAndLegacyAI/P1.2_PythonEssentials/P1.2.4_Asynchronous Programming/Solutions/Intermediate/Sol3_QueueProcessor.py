"""
Solution: Intermediate Assignment 3 - Async Queue Processor
"""

import asyncio

# Input data
items = ["file1", "file2", "file3", "file4", "file5"]

async def worker(name, queue):
    while True:
        try:
            item = await queue.get()
        except asyncio.CancelledError:
            break
        print(f"{name} processing {item}")
        await asyncio.sleep(0.3)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    for item in items:
        await queue.put(item)

    workers = [asyncio.create_task(worker(f"Worker-{i+1}", queue)) for i in range(2)]

    await queue.join()
    for w in workers:
        w.cancel()

asyncio.run(main())
