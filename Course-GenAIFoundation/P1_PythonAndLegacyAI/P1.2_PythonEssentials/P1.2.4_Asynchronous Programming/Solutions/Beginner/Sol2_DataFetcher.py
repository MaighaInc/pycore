"""
Solution: Beginner Assignment 2 - Async Data Fetcher
"""

import asyncio
import random

# Input data
urls = ["/users", "/orders", "/products"]

async def fetch_data(url):
    await asyncio.sleep(random.uniform(0.2, 0.8))
    return f"Fetched {url}"

async def main():
    results = await asyncio.gather(*(fetch_data(url) for url in urls))
    for result in results:
        print(result)

asyncio.run(main())
