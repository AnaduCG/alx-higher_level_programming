#!/usr/bin/python3


def magic_calculation(a, b):
    """a function hat prints python bytecode

    Args:
        a (int): arg 1
        b (int): arg 2

    Raises:
        Exception: _description_

    Returns:
        int: result of equation performed by the
        function to get desired bytecode output
    """
    result = 0

    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
        except Exception():
            result = b + a
            break

    return result
