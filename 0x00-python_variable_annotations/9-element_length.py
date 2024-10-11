#!/usr/bin/env python3
"""
This module provides a utility function to calculate the
lengths of elements in a given iterable.
The `element_length` function returns a list of tuples,
each containing an element and its corresponding length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in the input iterable.

    This function takes an iterable of sequences
    (such as lists or strings) and returns a list of tuples.
    Each tuple contains the original element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences
                                 (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each
        tuple contains an element from the
        input iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]
