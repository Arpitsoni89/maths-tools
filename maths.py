"""
Basic arithmetic operations module.

This module provides simple implementations of common mathematical operations.
All functions accept numeric inputs (int or float) and return numeric outputs.
"""

from typing import Union

# Type alias for numeric types
Number = Union[int, float]


def addition(a: Number, b: Number) -> Number:
    """
    Add two numbers.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b

    Example:
        >>> addition(5, 3)
        8
        >>> addition(2.5, 1.5)
        4.0
    """
    return a + b


def subtraction(a: Number, b: Number) -> Number:
    """
    Subtract b from a.

    Args:
        a: First number (int or float)
        b: Number to subtract (int or float)

    Returns:
        Difference of a - b

    Example:
        >>> subtraction(10, 4)
        6
        >>> subtraction(5.5, 2.5)
        3.0
    """
    return a - b


def multiplication(a: Number, b: Number) -> Number:
    """
    Multiply two numbers.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Product of a and b

    Example:
        >>> multiplication(6, 7)
        42
        >>> multiplication(2.5, 4)
        10.0
    """
    return a * b


def division(a: Number, b: Number) -> float:
    """
    Divide a by b.

    Args:
        a: Dividend (int or float)
        b: Divisor (int or float)

    Returns:
        Quotient of a / b as float

    Raises:
        ZeroDivisionError: If b is zero

    Example:
        >>> division(20, 4)
        5.0
        >>> division(10, 3)
        3.3333333333333335
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def modulus(a: Number, b: Number) -> Number:
    """
    Return the remainder of a divided by b.

    Args:
        a: Dividend (int or float)
        b: Divisor (int or float)

    Returns:
        Remainder of a % b

    Raises:
        ZeroDivisionError: If b is zero

    Example:
        >>> modulus(17, 5)
        2
        >>> modulus(10, 3)
        1
    """
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus with zero divisor")
    return a % b


def floor_division(a: Number, b: Number) -> int:
    """
    Return the floor division of a by b.

    Args:
        a: Dividend (int or float)
        b: Divisor (int or float)

    Returns:
        Floor of a / b as integer

    Raises:
        ZeroDivisionError: If b is zero

    Example:
        >>> floor_division(17, 5)
        3
        >>> floor_division(20, 4)
        5
    """
    if b == 0:
        raise ZeroDivisionError("Cannot perform floor division with zero divisor")
    return a // b
