#!/usr/bin/python3
"""a python class that handles Exception
        with an area() method
"""


class BaseGeometry:
    """a python class with an area(self) method
    """

    def area(self):
        """method that calculates the the area of the
            BaseGeometry class

        Raises:
            Exception: error if the area method isn't implemented
        """
        raise Exception("area() is not implemented")
