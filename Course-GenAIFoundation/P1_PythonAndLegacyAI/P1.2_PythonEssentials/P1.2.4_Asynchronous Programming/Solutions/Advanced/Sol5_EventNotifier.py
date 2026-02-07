"""
Solution: Advanced Assignment 5 - Async Event Notifier
"""

import asyncio

# Input data
events = [
    ("login", {"user": "alice"}),
    ("upload", {"file": "report.pdf"}),
    ("logout", {"user": "alice"})
]

class EventBus:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event, handler):
        self.handlers.setdefault(event, []).append(handler)

    async def emit(self, event, data):
        tasks = [handler(event, data) for handler in self.handlers.get(event, [])]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if isinstance(result, Exception):
                print(f"Handler error: {result}")

async def log_handler(event, data):
    await asyncio.sleep(0.1)
    print(f"[log] {event}: {data}")

async def email_handler(event, data):
    await asyncio.sleep(0.1)
    print(f"[email] {event}: {data}")

async def main():
    bus = EventBus()
    bus.subscribe("login", log_handler)
    bus.subscribe("login", email_handler)
    bus.subscribe("upload", log_handler)
    bus.subscribe("logout", log_handler)

    for event, data in events:
        await bus.emit(event, data)

asyncio.run(main())
