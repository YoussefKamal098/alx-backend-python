#!/usr/bin/env python3
"""
This module provides a function to sum a list of floating-point numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the floats in the list.
    """
    return sum(input_list)
