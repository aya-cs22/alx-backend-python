#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """The coroutine will loop 10 times"""
    res = [item async for item in async_generator()]
    return res
