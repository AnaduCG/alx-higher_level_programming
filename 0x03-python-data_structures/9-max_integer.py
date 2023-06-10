#!/usr/bin/python3
""" max_integer() - a function that finds the
                    biggest integer of a list.
    my_list=[]: list to be handled
"""


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max
