#!/usr/bin/env python3
"""
This module contains an example of an asynchronous generator.
"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random
    floating-point numbers between 0 and 10.

    This function generates 10 random numbers asynchronously.
    It waits 1 second before yielding each number.

    Yields:
        float: A random floating-point number
               between 0 and 10 after a 1-second delay.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
