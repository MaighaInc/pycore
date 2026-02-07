"""
Solution: Advanced Assignment 3 - Async Queue Processor
"""

import asyncio

# Input data
items = ["file1", "file2", "file3", "file4", "file5", "file6"]
workers = 3

async def producer(queue, items, workers):
    for item in items:
        await queue.put(item)
    for _ in range(workers):
        await queue.put(None)

async def consumer(name, queue):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            print(f"{name} exiting")
            break
        print(f"{name} processing {item}")
        await asyncio.sleep(0.2)
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producer_task = asyncio.create_task(producer(queue, items, workers))
    consumer_tasks = [asyncio.create_task(consumer(f"Worker-{i+1}", queue)) for i in range(workers)]

    await producer_task
    await queue.join()

    await asyncio.gather(*consumer_tasks)

asyncio.run(main())
