#!/usr/bin/env python3

"""
This module provides a utility function to 'zoom' into a tuple of
integers by repeating each element a specified number of times.
The `zoom_array` function allows scaling of the tuple elements by a
given factor, and returns the zoomed version as a list.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Repeats each element of a tuple a specified number of times.

    This function takes a tuple of integers and
    repeats each element by the specified `factor`.
    The result is a list with each element repeated consecutively.

    Args:
        lst (Tuple[int, ...]): A tuple of integers to be zoomed in on.
        factor (int, optional): The number of times each element
        should be repeated. Defaults to 2.

    Returns:
        List[int]: A list containing the repeated elements of the tuple.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, int(3.0))
