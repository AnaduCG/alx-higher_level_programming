#!/usr/bin/python3
"""element_at() - a function that
                retrieves an element from a list like in C
    my_list: the list to be handles by the fucntion
    idx: index of the element to be retrived fom the list
"""


def element_at(my_list, idx):
    if (idx < 0) or (idx >= len(my_list)):
        return(None)
    return my_list[idx]
