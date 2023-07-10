#!/usr/bin/python3


def lookup(obj):
    """_summary_

    Args:
        obj (class): parent class being inherited

    Returns:
        list: the list of available attributes and
            methods of an object
    """
    return dir(obj)
