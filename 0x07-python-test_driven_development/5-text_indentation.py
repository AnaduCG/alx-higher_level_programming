#!/usr/bin/python3
"""writing a function to indent a set of strings
"""


def text_indentation(text):
    """printing strings in a line and adding double 'newline'
    where '., :, .' are found

    Args:
        text (str): set of strings to be indented

    Raises:
        TypeError: invalid  datatype
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    line = ""
    for i in text:
        line += i
        if line[-1] in (".", "?", ":"):
            print("{}{}".format(line.strip(), "\n"))
            line = ""
    if line:
        print("{}".format(line.strip()), end="")
