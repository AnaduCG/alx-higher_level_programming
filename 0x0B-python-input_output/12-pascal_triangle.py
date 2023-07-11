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

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
