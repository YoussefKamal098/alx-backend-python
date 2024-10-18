#!/usr/bin/env python3
"""
Module to create asynchronous tasks for waiting with random delays.

This module provides a function to spawn an asynchronous task that waits
for a random amount of time, utilizing the `wait_random` function from
the `0-basic_async_syntax` module.

"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task to wait for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: An asyncio task that runs the `wait_random`
                       function with the specified max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
