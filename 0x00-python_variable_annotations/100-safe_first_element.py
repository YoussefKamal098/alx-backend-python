#!/usr/bin/env python3
"""
This module provides a function `safe_first_element` that returns the
first element of a sequence if it exists, otherwise returns None.
It uses duck-typed annotations to allow for flexible input types.
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists,
    otherwise returns None.

    Args:
        lst (Sequence[Any]): A sequence of elements of any type.

    Returns:
        Union[Any, None]: The first element of the sequence if
                          it's not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
