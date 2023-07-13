#!/usr/bin/python3
"""creating a student class
"""

class Student:
    """class representation of a student
    """
    def __init__(self, first_name, last_name, age):
        """instantiation in python

        Args:
            first_name (str): Student first name public instance
            last_name (str):  Student last name public instance
            age (int):  Student age public instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieves a dictionary
        representation of a Student instance

        Args:
            attrs (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        if attrs is None:
            return self.__dict__

        if not isinstance(attrs, list):
            return

        attribute_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                attribute_dict[attr] = self.__dict__[attr]

        return attribute_dict
