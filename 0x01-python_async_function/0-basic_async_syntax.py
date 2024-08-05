#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ that waits for a random delay between 0 and max_delay"""
    random_folat = random.uniform(0, max_delay)
    await asyncio.sleep(random_folat)
    return random_folat
