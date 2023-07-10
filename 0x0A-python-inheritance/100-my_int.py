#!/usr/bin/python3
"""python class that inverts == and !=
"""


class MyInt(int):
    """ a class MyInt that inherits from int

    Args:
        int (object): python int object
    """
    def __eq__(self, value):
        """python equal-to method

        Args:
            value (int): value to be compared

        Returns:
            method: inverted method for equal-to
                for the int object
        """
        return super().__ne__(value)

    def __ne__(self, value):
        """python notequal-to method

        Args:
            value (int): value to be compared

        Returns:
            method: inverted method for notequal-to
                for the int object
        """
        return super().__eq__(value)
