#!/usr/bin/python3
import numpy as np


def check_matrix(matrix, name):
    if len(matrix) == 0:
        raise ValueError("{} can't be empty".format(name))
    if isinstance(matrix[0], list):
        l = len(matrix[0])
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("{} must be a list of lists".format(name))
        if len(i) == 0:
            raise ValueError("{} can't be empty".format(name))
        if l != len(i):
            raise TypeError("each row of {} must be of the same size".format(name))
        for n in i:
            if type(n) not in (float, int):
                raise TypeError("{} should contain only integers or floats".format(name))


def lazy_matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    check_matrix(m_a, "m_a")
    check_matrix(m_b, "m_b")
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
