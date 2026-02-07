"""
Intermediate Assignment 1: Async Task Runner

Scenario:
Run multiple tasks concurrently and measure total runtime.

Objective:
Use asyncio.gather to run tasks in parallel.

Tasks:
1. Create async function wait_and_print(name, seconds)
2. Create async main() that runs all tasks concurrently
3. Measure total runtime using asyncio.get_event_loop().time()
4. Print total duration

Inputs:
tasks = [
    ("Task A", 1),
    ("Task B", 2),
    ("Task C", 1)
]

Expected Output (sample):
Starting Task A
Starting Task B
Starting Task C
Finished Task A
Finished Task C
Finished Task B
Total runtime: ~2s

Hints:
- Use asyncio.gather
- Use loop.time() for timing

Rubric:
- Correct concurrent execution: 50%
- Correct timing: 30%
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

