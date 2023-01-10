#!/usr/bin/python3
"""Defines a function, ``pascal_triangle``"""


def factorial(n):
    """Calculates the factorial of n"""
    if (n == 0):
        return (1)

    return (n * factorial(n - 1))


def combination(n=0, r=0):
    """Calculates the Combination, ``nCr``

    Args:
        n (int): total number of objects in the set
        r (int): number of choosing objects from the set
    Return:
        The calculated combination
    """
    c = factorial(n) // (factorial(n - r) * factorial(r))
    return (c)


def pascal_triangle(n):
    """Returns a list of lists of integers representing the
    Pascal's triangle of n"""
    triangle = []

    for m in range(n):
        triangle.append([combination(m, b) for b in range(m+1)])

    return (triangle)
