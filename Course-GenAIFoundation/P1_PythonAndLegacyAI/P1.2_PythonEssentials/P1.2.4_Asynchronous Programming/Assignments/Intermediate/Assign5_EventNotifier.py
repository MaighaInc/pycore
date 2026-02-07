"""
Intermediate Assignment 5: Async Event Notifier

Scenario:
Broadcast events to multiple async handlers concurrently.

Objective:
Use asyncio.gather for event fan-out.

Tasks:
1. Create async function notify_handler(handler, event)
2. Create async function broadcast(event, handlers)
3. Run broadcasts for all events

Inputs:
events = ["login", "upload", "logout"]
handlers = ["email", "sms", "log"]

Expected Output (sample):
email handled login
sms handled login
log handled login
...

Hints:
- Use asyncio.gather
- Simulate delay with asyncio.sleep

Rubric:
- Correct concurrency: 40%
- Proper broadcast logic: 40%
- Output formatting: 20%
"""

import asyncio

# Input data
events = ["login", "upload", "logout"]
handlers = ["email", "sms", "log"]

# Your code here

