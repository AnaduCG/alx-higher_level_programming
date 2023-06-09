#!/usr/bin/python3
"""print_matrix_integer() - a function that  prints
                            a matrix of integers.
    matrix=[[]]: the array of integers matrix to be handled
"""


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for n in i:
            print("{:2d}".format(n), end='')
        print('$')
