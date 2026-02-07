"""
Intermediate Assignment 3: Async Queue Processor

Scenario:
Process items using an asyncio.Queue with multiple workers.

Objective:
Use asyncio.Queue and worker coroutines.

Tasks:
1. Create an asyncio.Queue and add all items
2. Create worker coroutine that processes items until queue is empty
3. Start 2 workers and wait for completion

Inputs:
items = ["file1", "file2", "file3", "file4", "file5"]

Expected Output:
Workers should process all items, order may vary.

Hints:
- Use queue.get() and queue.task_done()
- Cancel workers after queue is done

Rubric:
- Correct queue usage: 50%
- Proper worker setup: 30%
- Output formatting: 20%
"""

import asyncio

# Input data
items = ["file1", "file2", "file3", "file4", "file5"]

# Your code here

