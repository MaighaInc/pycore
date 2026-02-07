"""
Advanced Assignment 3: Async Queue Processor

Scenario:
Build a producer-consumer system with graceful shutdown.

Objective:
Use asyncio.Queue with multiple consumers and a sentinel value.

Tasks:
1. Create producer that enqueues items then a sentinel (None)
2. Create multiple consumers that stop on sentinel
3. Start producer and consumers concurrently
4. Ensure all tasks finish cleanly

Inputs:
items = ["file1", "file2", "file3", "file4", "file5", "file6"]
workers = 3

Expected Output:
Each worker processes multiple items, then exits.

Hints:
- Each consumer should re-add sentinel for other workers or count sentinels
- Use queue.join() for synchronization

Rubric:
- Correct producer/consumer setup: 40%
- Proper shutdown: 30%
- Output formatting: 30%
"""

import asyncio

# Input data
items = ["file1", "file2", "file3", "file4", "file5", "file6"]
workers = 3

# Your code here

