#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
    importing the BaseGeometry class for inheritance
"""


class Rectangle(BaseGeometry):
    """a Rectangle class

    Args:
        BaseGeometry (class): inherited class
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
