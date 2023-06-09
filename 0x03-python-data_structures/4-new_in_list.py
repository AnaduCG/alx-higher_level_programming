#!/usr/bin/python3
"""new_in_list() - a function that replaces an element in
                a list at a specific position without
                modifying the original list (like in C)
    my_list: list to be handled
    idx: index of the new list to be modified
    element: value to be added to the new list copy
"""


def new_in_list(my_list, idx, element):
    my_list_copy = my_list.copy()
    if (idx < 0) or (idx >= len(my_list)):
        return my_list_copy
    my_list_copy[idx] = element
    return my_list_copy
