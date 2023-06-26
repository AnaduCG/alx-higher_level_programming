#!/usr/bin/python3
def safe_print_division(a, b):
    """a function that divides 2 integers and prints the result.

    Args:
        a (int): numerator
        b (int): denominator
    """
    try:
        div = a/b
    except (ZeroDivisionError):
        div = None
    finally:
        print("inside result {}".format(div))
    return div
