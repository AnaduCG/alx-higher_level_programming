#!/usr/bin/python3
"""importing json and StringIO
"""
import json
from io import StringIO
"""reading from a json file
"""


def load_from_json_file(filename):
    """function that creates an Object from
    a “JSON file”:

    Args:
        filename (str): name of file to read from

    Returns:
        obj: json object
    """
    with open(filename, "r", encoding="utf-8") as f:
        read = f.read()
        io = StringIO(read)
        return json.load(io)
