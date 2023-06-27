#!/usr/bin/python3


class Square:
    def __init__(self, size)
    if is not isinstance(size, int):
        TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        self.__size = size
    @property
    def size(self):
        return self.__size
