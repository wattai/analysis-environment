# -*- coding: utf-8 -*-

__all__ = ["add", "sub"]


def add(a: float, b: float) -> float:
    """Add two values.

    Args:
        a (float): 1st argument.
        b (float): 2nd argument.

    Returns:
        float: summation.

    Examples:
        How to use.

        >>> add(1.0, 2.5)
        3.5
    """
    return a + b


def sub(a: float, b: float) -> float:
    """Sub two values.

    Args:
        a (float): 1st argument.
        b (float): 2nd argument.

    Returns:
        float: subtract.

    Examples:
        How to use.

        >>> sub(3.0, 1.2)
        1.8
    """
    return a - b
