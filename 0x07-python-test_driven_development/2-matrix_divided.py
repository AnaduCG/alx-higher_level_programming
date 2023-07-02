#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""dividing the values of an array matrix
"""


def is_matrix(matrix):
    """a function that checks if a value data type is a matrix

    Args:
        matrix (any): value to be checked

    Returns:
        Bool: returns True if the value is a matrix array otherwise False
    """
    if isinstance(matrix, list) and\
       all(isinstance(row, list) for row in matrix):
        return True
    return False


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (array): array of matrix whose values are to be divided
        div (int, float): value to be used for the division

    Raises:
        TypeError: if the passed matrix value is an invalid matrix
        TypeError: if the div value passed id not an in nor a float
        ZeroDivisionError: if div is 0
        TypeError: if matrix length aren't equal
        TypeError: if matrix contains non number value(int, float)

    Returns:
        array: returns the matrix with divided values
    """
    new_matrix = []

    if not is_matrix(matrix):
        raise TypeError("matrix must be a matrix\
(list of lists) of integers/floats")

    num = len(matrix[0])
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for arr in matrix:
        if num != len(arr):
            raise TypeError("Each row of the matrix must have the same size")
        for item in arr:
            if type(item) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
        new_matrix.append(list(map(lambda x: round(x / div, 2), arr)))
    return new_matrix
