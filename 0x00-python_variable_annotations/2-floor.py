#!/usr/bin/env python3
"""
This module provides a function to calculate the floor of a
floating-point number.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): The number to calculate the floor of.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
