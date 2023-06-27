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
    def __init__(self, size=0):
        """attribute instantiation for the Square class

        Args:
            size (int, optional): private instance attribute
            . Defaults to 0.

        Raises:
            TypeError: size must be an integer,
            ValueError: if size is less than 0, raise
        """
        self.__size = size

    @property
    def size(self):
        """property setter to retrieve the size attribute

        Returns:
            int: returns the Square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """property setter

        Args:
            value (int): private instance attribute

        Raises:
            TypeError: size must be an integer
            ValueError: if size is less than 0,
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """public instance method

        Returns:
            _type_: _description_
        """
        return self.__size ** 2
