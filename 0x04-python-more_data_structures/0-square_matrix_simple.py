#!/usr/bin/python3
"""square_matrix_simple - function that computes
                            the square value of all integers of a matrix.
    @matrix: list value to be handled
"""


def square_matrix_simple(matrix=[]):
    pro = []
    if not matrix:
        return
    for i in  matrix:
        pro.append(list(map(lambda x: x ** 2, i)))
    return pro
