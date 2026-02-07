"""
Advanced Assignment 5: Async Event Notifier

Scenario:
Build a simple async event bus with multiple subscribers.

Objective:
Create a publish/subscribe system using async callbacks.

Tasks:
1. Create EventBus class with subscribe(event, handler) and emit(event, data)
2. Handlers should be async functions
3. Emit should run all handlers concurrently
4. Handle handler errors without stopping others

Inputs:
events = [
    ("login", {"user": "alice"}),
    ("upload", {"file": "report.pdf"}),
    ("logout", {"user": "alice"})
]

Expected Output (sample):
[log] login: {'user': 'alice'}
[email] login: {'user': 'alice'}
...

Hints:
- Use asyncio.gather(..., return_exceptions=True)

Rubric:
- Correct event bus design: 40%
- Correct async handling: 40%
- Output formatting: 20%
"""

import asyncio

# Input data
events = [
    ("login", {"user": "alice"}),
    ("upload", {"file": "report.pdf"}),
    ("logout", {"user": "alice"})
]

# Your code here

