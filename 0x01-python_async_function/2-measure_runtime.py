#!/usr/bin/env python3
"""
Module to measure the execution time of asynchronous functions.

This module provides a function to measure the time taken by the
`wait_n` function to complete its execution. The `wait_n` function
is imported from the `1-concurrent_coroutines.py` module, which
spawns asynchronous tasks to wait for random delays.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines.py').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the execution time of the `wait_n` function.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for `wait_random`.

    Returns:
        float: The total time taken for the `wait_n` function to complete.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return end - start
