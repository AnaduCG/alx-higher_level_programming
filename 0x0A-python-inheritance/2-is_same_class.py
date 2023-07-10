#!/usr/bin/python3
"""function that compares the class type of an object
"""


def is_same_class(obj, a_class):
    """ a function that checks if an object is exactly
        an instance of a class

    Args:
        obj (object): an object of a class
        a_class (class): class to be used for the check

    Returns:
        Bool:  True if the object is exactly an instance
                of the specified class ; otherwise False.
    """
    return type(obj) is a_class
