#!/usr/bin/python3
"""print_list_integer - a function that prints the
                        contetnt of a list with integer values
    my_list[]: list to be handled by the function
"""


def print_list_integer(my_list=[]):
    for i in my_list:
        print("{}".format(i), end='\n')
