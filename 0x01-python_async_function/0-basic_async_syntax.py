#!/usr/bin/env python3

""" The basics of async """

import random
import asyncio


async def wait_random(max_dealy=10):
    """ wait random time between 0 and max delay then return it """
    delay = random.uniform(0, max_dealy)
    await asyncio.sleep(delay)
    return delay