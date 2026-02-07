"""
Mini Project 1: Async Log Processing Pipeline (Solution)
"""

import asyncio

# Sample log data
log_data = [
    "2026-02-07 10:00:01 INFO System started",
    "2026-02-07 10:05:12 WARNING Disk space low",
    "2026-02-07 10:10:30 ERROR File not found",
    "2026-02-07 10:12:45 INFO User login",
    "2026-02-07 10:15:10 ERROR Database timeout",
    "2026-02-07 10:20:00 INFO Job completed"
]

async def write_logs(filename, lines):
    def _write():
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(lines))
    await asyncio.to_thread(_write)

async def read_logs(filename):
    def _read():
        with open(filename, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    return await asyncio.to_thread(_read)

def count_levels(lines):
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    for line in lines:
        parts = line.split()
        if len(parts) >= 3 and parts[2] in counts:
            counts[parts[2]] += 1
    return counts

def write_summary(filename, total, counts):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Total logs: {total}\n")
        for level, count in counts.items():
            file.write(f"{level}: {count}\n")

async def main():
    print("=" * 50)
    print("ASYNC LOG PIPELINE")
    print("=" * 50)

    await write_logs("system.log", log_data)
    lines = await read_logs("system.log")
    counts = count_levels(lines)

    total = len(lines)
    print(f"Total logs: {total}")
    for level, count in counts.items():
        print(f"{level}: {count}")

    write_summary("log_summary.txt", total, counts)
    print("Summary saved to: log_summary.txt")
    print("=" * 50)

asyncio.run(main())
