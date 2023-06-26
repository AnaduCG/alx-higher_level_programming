#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """function that prints the first x elements of a list and only integers.

    Args:
        my_list: list to be handled.
        x (int, optional): _description_. Defaults to 0.

    Returns:
        int: Returns the real number of integers printed
    """
    count = j = 0
    for i in my_list[:x]:
        try:
            print("{:d}".format(i), end="")
            count += 1
            j += 1
        except (TypeError, ValueError):
            j += 1
    if j != x:
        raise IndexError()
    print()
    return count
