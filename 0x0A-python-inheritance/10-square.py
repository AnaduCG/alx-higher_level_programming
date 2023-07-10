#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

"""
importing the Rectangle module for inheritance
"""


class Square(Rectangle):
    """Square class the defines a square

    Args:
        Rectangle (class): inherited parent class
    """

    def __init__(self, size):
        """python instantiation method

        Args:
            size (int): size of the Square class
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """method that calculates the area of the
            Square class

        Returns:
            int: returns the calculated area of
                the Square class
        """
        return self.__size ** 2
