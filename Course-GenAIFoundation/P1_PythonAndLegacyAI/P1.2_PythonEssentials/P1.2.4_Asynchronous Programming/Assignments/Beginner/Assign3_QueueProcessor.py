"""
Beginner Assignment 3: Async Queue Processor

Scenario:
Process tasks in a simple queue with async functions.

Objective:
Use asyncio to process items in order.

Tasks:
1. Create async function process_item(item)
2. Simulate processing with asyncio.sleep
3. Create async function process_queue(items)
4. Process each item sequentially with await

Inputs:
items = ["file1", "file2", "file3"]

Expected Output:
Processing file1
Done file1
Processing file2
Done file2
Processing file3
Done file3

Hints:
- Use async for sequential processing
- Use await inside loop

Rubric:
- Correct async functions: 40%
- Correct processing order: 40%
- Output formatting: 20%
"""

import asyncio

# Input data
items = ["file1", "file2", "file3"]

# Your code here

