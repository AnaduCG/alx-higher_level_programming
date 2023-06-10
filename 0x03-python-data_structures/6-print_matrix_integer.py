#!/usr/bin/python3
"""print_matrix_integer() - a function that  prints
                            a matrix of integers.
    matrix=[[]]: the array of integers matrix to be handled
"""


def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print('$')
        return
    for i in matrix:
        for j in i:
            print("{:2d}".format(j), end='')
        print('$')
