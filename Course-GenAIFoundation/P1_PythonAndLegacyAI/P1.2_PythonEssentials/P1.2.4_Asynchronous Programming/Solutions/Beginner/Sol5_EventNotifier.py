"""
Solution: Beginner Assignment 5 - Async Event Notifier
"""

import asyncio

# Input data
events = ["login", "upload", "logout"]

async def notify(event):
    print(f"Notifying: {event}")
    await asyncio.sleep(0.2)

async def main():
    for event in events:
        await notify(event)

asyncio.run(main())
