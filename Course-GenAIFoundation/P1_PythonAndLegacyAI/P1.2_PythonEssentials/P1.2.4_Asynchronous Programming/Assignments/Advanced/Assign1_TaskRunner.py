"""
Advanced Assignment 1: Async Task Runner

Scenario:
Manage tasks with timeouts and cancellation.

Objective:
Use asyncio.create_task, asyncio.wait, and cancellation handling.

Tasks:
1. Create async function wait_and_print(name, seconds)
2. Start tasks concurrently
3. Use asyncio.wait with timeout=2.0
4. Cancel any pending tasks and handle cancellation
5. Print completed vs cancelled tasks

Inputs:
tasks = [
    ("Task A", 1),
    ("Task B", 3),
    ("Task C", 2)
]

Expected Output (sample):
Finished Task A
Finished Task C
Cancelled Task B

Hints:
- Use asyncio.wait(return_when=asyncio.ALL_COMPLETED)
- Call task.cancel() for pending tasks
- Catch asyncio.CancelledError inside tasks

Rubric:
- Correct task management: 40%
- Proper cancellation: 30%
- Output formatting: 30%
"""

import asyncio

# Input data
tasks = [
    ("Task A", 1),
    ("Task B", 3),
    ("Task C", 2)
]

# Your code here

