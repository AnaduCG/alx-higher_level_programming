#!/usr/bin/python3
"""a class Rectangle that defines a rectangle

    Raises:
        TypeError: the rectangle width must be an integer
        ValueError: the rectangle width must be greater or == 0
        TypeError: the rectangle height must be an integer
        ValueError: the rectangle height must be >= 0

    Returns:
        tuple: values for Rectangle instance
"""


class Rectangle:
    """a class Rectangle that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """initialization  of private instances

        Args:
            width (int, optional): Rectangles width. Defaults to 0.
            height (int, optional): Rectangles height. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getting the with property of the rectangle class

        Returns:
            int: Rectangle width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setting the rectangle width

        Args:
            value (int): value to be passed from the instance of rectangle

        Raises:
            TypeError: the passed value must be an integer
            ValueError: the passed value must not be a negative value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getting the height property of the rectangle class

        Returns:
            int: Rectangle height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setting the rectangle width

        Args:
            value (int): value to pe passed from the instance of rectangle

        Raises:
            TypeError: the passed value must be an integer
            ValueError: the passed value must not be a negative value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method of the Rectangle class which calculates
            the area of a Rectangle instance

        Returns:
            int: the total area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """method which calculates the perimeter of the Rectangle instance

        Returns:
            int: perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """built-in python method to print string from an object instance

        Returns:
            str: rectangle in string format
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        shape = ""
        for _ in range(self.__height):
            shape += ("#" * self.__width) + "\n"
        return shape[:-1]

    def __repr__(self):
        """built-in python method that converts an object instance to int

        Returns:
            tuple: values of the Rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
