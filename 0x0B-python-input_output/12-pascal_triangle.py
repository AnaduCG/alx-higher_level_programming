#!/usr/bin/python3
"""Oascal triangle algorithm
"""


def pascal_triangle(n):
    """function that prints the
    oascal troangle of ints

    arg n
    int: triangle size
    Returns:
    arr: array of ints
    """
    if n <= 0:
        return []

    tr = [[1]]
    for i in range(1, n):
        rw = [1]
        for j in range(1, i):
            rw.append(tr[i-1][j-1] + tr[i-1][j])
        rw.append(1)
        tr.append(rw)

    return tr
