#!/usr/bin/env python3

"""
This module provides asynchronous functions for managing and executing
concurrent tasks using the asyncio library.
"""

import asyncio
from typing import AsyncGenerator, List

wait_random = __import__('0-basic_async_syntax').wait_random


async def custom_as_completed(
        tasks: List[asyncio.Task]
) -> AsyncGenerator[asyncio.Task, None]:
    """
    Simulate asyncio.as_completed by yielding tasks as they complete.

    Args:
        tasks (List[asyncio.Task]): A list of asyncio tasks to monitor.

    Yields:
        asyncio.Task: The completed task.
    """
    pending = set(tasks)

    while pending:
        done, pending = await asyncio.wait(
            pending,  return_when=asyncio.FIRST_COMPLETED)

        for task in done:
            yield task


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `wait_random` `n` times with the specified `max_delay`
    and return the list of delays in the order they were completed.

    Args:
        n (int): The number of times to spawn `wait_random`.
        max_delay (int): The maximum delay for `wait_random`.

    Returns:
        List[float]: A list of float values representing the delays,
                     in the order they were completed.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    return [await task async for task in custom_as_completed(tasks)]
