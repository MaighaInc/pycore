"""
Solution: Advanced Assignment 2 - Async Data Fetcher
"""

import asyncio

# Input data
requests = [
    ("/users", 0.8),
    ("/orders", 1.2),
    ("/products", 0.5),
    ("/reports", 2.0),
    ("/stats", 1.8)
]

semaphore = asyncio.Semaphore(3)

async def fetch_data(url, delay):
    async with semaphore:
        await asyncio.sleep(delay)
        return f"Success: {url}"

async def safe_fetch(url, delay):
    try:
        return await asyncio.wait_for(fetch_data(url, delay), timeout=1.5)
    except asyncio.TimeoutError:
        return f"Timeout: {url}"

async def main():
    results = await asyncio.gather(*(safe_fetch(url, delay) for url, delay in requests), return_exceptions=True)
    for result in results:
        print(result)

asyncio.run(main())
