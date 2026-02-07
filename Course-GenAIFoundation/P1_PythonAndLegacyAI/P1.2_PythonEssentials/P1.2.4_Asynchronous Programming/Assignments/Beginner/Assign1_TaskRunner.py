"""
Beginner Assignment 1: Async Task Runner

Scenario:
Run simple async tasks with delays to learn async/await basics.

Objective:
Create async functions and run them with asyncio.

Tasks:
1. Create async function wait_and_print(name, seconds)
2. Use asyncio.sleep(seconds)
3. Print when each task starts and ends
4. Run tasks sequentially using await

Inputs:
tasks = [
    ("Task A", 1),
    ("Task B", 2),
    ("Task C", 1)
]

Expected Output (order may follow sequential awaits):
Starting Task A
Finished Task A
Starting Task B
Finished Task B
Starting Task C
Finished Task C

Hints:
- Use async def and await
- Use asyncio.run(main())

Rubric:
- Correct async function: 40%
- Correct use of await: 40%
- Output formatting: 20%
"""

import asyncio

# Input data
tasks = [
    ("Task A", 1),
    ("Task B", 2),
    ("Task C", 1)
]

# Your code here

