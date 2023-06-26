#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """function that prints elements of an array up till a specifies index 'x'

    Args:
        my_list : the list whose values are to be printed.
        x (int, optional): index to stop at. Defaults to 0.

    Returns:
        int: number of elements printed
    """
    num_of_elem = 0
    i = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end=(''))
            num_of_elem += 1
        except IndexError:
            continue
    print('')
    return num_of_elem
