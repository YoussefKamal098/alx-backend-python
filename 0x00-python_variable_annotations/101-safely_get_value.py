#!/usr/bin/env python3
"""
This module provides a utility function to safely retrieve values from
a mapping (like a dictionary). The function allows specifying a
default value to return in case the requested key is not found in
the mapping. The module also uses Python's type hinting and
generics (`TypeVar`) to ensure flexibility
and consistency in return types.
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary-like mapping,
    with an optional default value.

    This function attempts to retrieve the value associated with a
    given key from the provided mapping (e.g., dictionary).
    If the key exists, it returns the corresponding value. Otherwise,
    it returns the default value provided,
    or `None` if no default is specified.

    Args:
        dct (Mapping[Any, Any]): The mapping (dictionary-like object)
        to search for the key.
        key (Any): The key to search for in the mapping.
        default (Union[T, None], optional): The value to return if the
        key is not found. Defaults to `None`.

    Returns:
        Union[Any, T]: The value corresponding to the key,
        or the `default` value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
