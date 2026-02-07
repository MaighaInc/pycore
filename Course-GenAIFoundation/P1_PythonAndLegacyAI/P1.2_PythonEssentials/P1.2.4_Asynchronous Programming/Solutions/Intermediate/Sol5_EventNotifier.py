"""
Solution: Intermediate Assignment 5 - Async Event Notifier
"""

import asyncio

# Input data
events = ["login", "upload", "logout"]
handlers = ["email", "sms", "log"]

async def notify_handler(handler, event):
    await asyncio.sleep(0.1)
    print(f"{handler} handled {event}")

async def broadcast(event, handlers):
    await asyncio.gather(*(notify_handler(h, event) for h in handlers))

async def main():
    for event in events:
        await broadcast(event, handlers)

asyncio.run(main())
