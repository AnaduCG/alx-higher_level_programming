#!/usr/bin/python3
"""printing squares
"""


def print_square(size):
    """function that prints a square shape using '#'

    Args:
        size (int): number of '#' to be printed in order to form a square

    Raises:
        TypeError: if size isn't a valid datatype
        ValueError: if size is less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format("#" * size))
