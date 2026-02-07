"""
Beginner Assignment 5: Async Event Notifier

Scenario:
Send notifications asynchronously when events occur.

Objective:
Create async notifier functions and call them in sequence.

Tasks:
1. Create async function notify(event)
2. Simulate sending with asyncio.sleep
3. Create async main() that notifies all events

Inputs:
events = ["login", "upload", "logout"]

Expected Output:
Notifying: login
Notifying: upload
Notifying: logout

Hints:
- Use asyncio.run(main())

Rubric:
- Correct async flow: 40%
- Proper use of await: 40%
- Output formatting: 20%
"""

import asyncio

# Input data
events = ["login", "upload", "logout"]

# Your code here

