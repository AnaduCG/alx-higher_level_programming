#!/usr/bin/python3
"""writing to a file in python
"""


def write_file(filename="", text=""):
    """function that creates and write into a file

    Args:
        filename (str, optional): name of the file
        to be written into. Defaults to "".
        text (str, optional): content to be written
        into the file. Defaults to "".

    Returns:
        int: number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        written = f.write(text)
        return written
