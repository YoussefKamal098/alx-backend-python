#!/usr/bin/env python3
"""
This module provides a function to sum a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floating-point numbers.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing
        integers and floats.

    Returns:
        float: The sum of the numbers in the list.
    """
    return sum(mxd_lst)
