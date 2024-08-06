#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension



async def measure_runtime() -> float:
    """execute async_comprehension 4 times in parallel using asyncio.gather."""
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.perf_counter() - start_time