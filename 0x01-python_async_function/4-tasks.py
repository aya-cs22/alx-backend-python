#!/usr/bin/env python3
"""Tasks"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """Return the list of all the delays (float values)"""
    tasks = [task_wait_random(max_delay) for i in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
