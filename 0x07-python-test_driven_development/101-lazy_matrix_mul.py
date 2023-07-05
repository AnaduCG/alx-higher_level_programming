#!/usr/bin/python3
import numpy as np


"""a program tat multiplies the values of a matrix and returns
                a new matrix containing the value from the result
                of the matrix multiplication
"""


def check_matrix(matrix, name):
    """a function that checks fro error in
            the matrix multiplication program

    Args:
        matrix (list): list of matrix to be checked
        name (string): name of the list being
                        passed fom the calling
                        function

    Raises:
        ValueError: if the matrix is found to be empty
        TypeError: if the matrix is not a list of lists
        ValueError: if the matrix array is empty
        TypeError: if the matrix array do not have same length
        TypeError: if the list of list do not contain a number value
    """
    if len(matrix) == 0:
        raise ValueError("{} can't be empty".format(name))
    if isinstance(matrix[0], list):
        length = len(matrix[0])
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("{} must be a list of lists".format(name))
        if len(i) == 0:
            raise ValueError("{} can't be empty".format(name))
        if length != len(i):
            raise TypeError("each row of {} must be of\
the same size".format(name))
        for n in i:
            if type(n) not in (float, int):
                raise TypeError("{} should contain only\
integers or floats".format(name))


"""function that prints matrix using numpy
"""


def lazy_matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices
            using numpy module

    Args:
        m_a (int): first matrix list
        m_b (int): second matrix list

    Raises:
        TypeError: if m_a is not a list type
        TypeError: if m_b is not a list type
        ValueError: if a unknown error occurs during
                        the program execution

    Returns:
        list: a new list containing the result of the
            multiplication of the two lists
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    check_matrix(m_a, "m_a")
    check_matrix(m_b, "m_b")
    try:
        result = np.matmul(m_a, m_b)
        return result
    except Exception:
        print("Shit!")
        raise ValueError("m_a and m_b can't be multiplied")
