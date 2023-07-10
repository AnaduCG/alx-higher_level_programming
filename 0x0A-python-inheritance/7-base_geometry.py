#!/usr/bin/python3


class BaseGeometry:
    """a class in python that has an area method
        and a integer_validator method
    """

    def area(self):
        """BaseGeometry method that raises an exception

        Raises:
            Exception: checks if area() method is implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """BaseGeometry method that validates a valid integer

        Args:
            name (str): name of the value passed
            value (int): value passed to be checked
                        if its a valid int

        Raises:
            TypeError: if the provided value is an invalid type(non int)
            ValueError: if the value is < 1
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
