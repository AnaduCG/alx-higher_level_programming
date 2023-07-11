#!/usr/bin/python3
"""reading a file in python
"""


def read_file(filename=""):
    """function that reads a file in python

    Args:
        filename (str, optional): file to be opened
        in read mode. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print("{}".format(line), end='')
