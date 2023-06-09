#!/usr/bin/python3
"""a python class that returns a formatted string
"""
Rectangle = __import__('9-rectangle').Rectangle
"""
getting the Rectangle module for inheritance
"""


class Square(Rectangle):
    """python definition of a square class

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
        """method that calculates the area of the Square class

        Returns:
            int: returns the calculated are of the Square class
        """
        return self.__size ** 2

    def __str__(self):
        """python method that returns a class instance in a string format

        Returns:
            str: output from the __str__ method
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
