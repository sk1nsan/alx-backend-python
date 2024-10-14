#!/usr/bin/env python3
""" The basics of async """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ wait random time between 0 and max delay then return it """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
