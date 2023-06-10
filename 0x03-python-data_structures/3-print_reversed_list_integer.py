#!/usr/bin/python3
"""print_reversed_list_integer() - a function that
                                prints the content of an array in reverse order
    my_list=[]: the list to be handled by the function
"""


def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        for i in reversed(my_list):
            print("{:d}".format(i))
