#!/usr/bin/python3
"""divisible_by_2() - a function that finds
                        all multiples of 2 in a list.
    my_list=[]: list to be handled
"""


def divisible_by_2(my_list=[]):
    new_list = [num % 2 == 0 for num in my_list]
    return new_list
