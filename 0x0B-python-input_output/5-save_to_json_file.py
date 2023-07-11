#!/usr/bin/python3
"""importing json
"""
import json
"""writing and saving to a json file
"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text
    file, using a JSON representation:

    Args:
        my_obj (obj): object to be written
        filename (str): name of file to write to
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
