#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
importing the BaseGeometry for inheritance
"""


class Rectangle(BaseGeometry):
    """Rectangle class

    Args:
        BaseGeometry (class): inherited parent class
    """

    def __init__(self, width, height):
        """python instantiation method

        Args:
            width (int): with of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """method that calculates teh area of the rectangle

        Returns:
            int: returns the calculated are of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """python method that returns a class instance
            in string format

        Returns:
            str: output from the __str__ method
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
