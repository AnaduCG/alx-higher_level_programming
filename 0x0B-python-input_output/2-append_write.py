#!/usr/bin/python3
"""appending to a file in python
"""


def append_write(filename="", text=""):
    """function that appends  input to a file

    Args:
        filename (str, optional): file to append to.
        Defaults to "".
        text (str, optional): text to be appended to the file
        . Defaults to "".

    Returns:
        int: number of characters appended to the file
    """
    with open(filename, "a+", encoding="utf-8") as f:
        added_chars = f.write(text)
        return added_chars
