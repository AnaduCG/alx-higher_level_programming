#!/usr/bin/python3
"""
Creating a class that returns a list object
"""

def lookup(obj):
    """A  class that prints lookup  list of available
        attributes and methods of an object

    Args:
        obj (class): parent class being inherited

    Returns:
        list: the list of available attributes and
            methods of an object
    """
    return dir(obj)
