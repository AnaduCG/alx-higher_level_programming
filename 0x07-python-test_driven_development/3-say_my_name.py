#!/usr/bin/python3
"""printing a users full name
"""


def say_my_name(first_name, last_name=""):
    """a function that prints user name with valid strings

    Args:
        first_name (str): user firstname
        last_name (str, optional): user lastname. Defaults to "".

    Raises:
        TypeError: if the firstname is not a valid type (string)
        TypeError: if the lastname is not a valid type (string)
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
