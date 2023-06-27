#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" a class Square that defines a square by: (based on 1-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):

    Raises:
        TypeError: size must be an integer,
        ValueError: if size is less than 0, raise
"""


class Square:
    """a class Square that defines a square
    """
    def __init__(self, size=0):
        """attribute instantiation for the Square class

        Args:
            size (int, optional): private instance attribute
            . Defaults to 0.

        Raises:
            TypeError: size must be an integer,
            ValueError: if size is less than 0, raise
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
