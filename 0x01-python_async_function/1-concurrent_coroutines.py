#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """return the list of all the delays (float values)"""
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    delays = await asyncio.gather(*tasks)
    sorted_delays = []
    while delays:
        min_delays = min(delays)
        sorted_delays.append(min_delays)
        delays.remove(min_delays)
    return (sorted_delays)
