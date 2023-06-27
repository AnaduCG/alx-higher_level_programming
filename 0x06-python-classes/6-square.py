#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""a class Square that defines a square
    the class is made up of one instantiation

    instances:
        __init__
        size
        area
"""


class Square:
    """a class Square that defines a square
    """
    def __init__(self, size)
    if is not isinstance(size, int):
        TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size

    @property
    def size(self):
        return self.__size
