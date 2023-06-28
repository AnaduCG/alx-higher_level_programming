#!/usr/bin/python3
"""A python class with a private attribute
    and instantiation
"""
class Square:
    """a class Square that defines a square
    """
    def __init__(self, size=0):
        """ creates a private instance attribute
        
        Args:
            self (): refers to the object itself
            size (): size of the Square to be initialization to
                    an object attribute
        """
        self.__size = size
