#!/usr/bin/python3
"""importing the json module
"""
import json
"""json representation of an object
"""


def to_json_string(my_obj):
    """function that returns the JSON
    representation of an object (string)

    Args:
        my_obj (str): string to be handled

    Returns:
        str: json string
    """
    return json.dumps(my_obj)
