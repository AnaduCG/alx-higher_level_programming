#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """ function that checks if an object is an instance of,
        or if the object is an instance of a class that inherited
        from, a specified class

    Args:
        obj (object): object of a class
        a_class (class): class to use for te check

    Returns:
        Bool:  returns True if the object is an instance of,
                or if the object is an instance of a class that
                inherited from, the specified class ; otherwise
                False
    """
    if isinstance(obj, a_class):
        return True
    return False
