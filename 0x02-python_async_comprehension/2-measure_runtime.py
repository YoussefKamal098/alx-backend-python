#!/usr/bin/env python3
"""
This module provides a function to measure the runtime of
executing asynchronous comprehensions concurrently.
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime for executing 10 asynchronous
    comprehensions concurrently.

    This function uses `asyncio.gather` to run 10 instances of
    `async_comprehension` in parallel.  It calculates the
    time taken to complete all the tasks using the `time.time()` function.

    Returns:
        float: The total runtime in seconds.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(10)))
    end = time.time()

    return end - start
