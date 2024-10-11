#!/usr/bin/env python3
"""
This module provides a function to convert a string and a number to a tuple.
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string and a number to a tuple containing the
    string and the square of the number.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The number to square.

    Returns:
        Tuple[str, float]: A tuple where the first element is k
                          and the second is the square of v.
    """
    return k, v ** 2
