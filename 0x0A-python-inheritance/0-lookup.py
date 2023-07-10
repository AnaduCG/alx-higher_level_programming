#!/usr/bin/python3
"""
Creating a function that returns a list object
"""


def lookup(obj):
    """A  function that prints lookup  list of available
        attributes and methods of an object

    Args:
        obj (object): parent class being inherited

    Returns:
        list: the list of available attributes and
            methods of an object
    """
    return dir(obj)
