#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""a class Square that defines a square
    the class is made up of one instantiation with
    a private instance attribute (size)
"""


class Square:
    """a class that defines a square
    """
    def __init__(self, size=0):
        """Instantiation with optional size

        Args:
            size (int): variable for the size of the square class
        """
        self.__size = size
