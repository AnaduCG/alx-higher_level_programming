#!/usr/bin/python3
"""
importing json and StringIO
"""
import json
from io import StringIO
"""getting object from json
"""


def from_json_string(my_str):
    """function that returns an object
    (Python data structure) represented by a
    JSON string:

    Args:
        my_str (str): json string

    Returns:
        obj: Python data structure
    """
    io = StringIO(my_str)
    return json.load(io)
