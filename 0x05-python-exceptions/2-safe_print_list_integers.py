#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """function that prints the first x elements of a list and only integers.

    Args:
        my_list: list to be handled.
        x (int, optional): _description_. Defaults to 0.

    Returns:
        int: Returns the real number of integers printed
    """
    i = 0
    num_of_ele = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end=(''))
            num_of_ele += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return num_of_ele
