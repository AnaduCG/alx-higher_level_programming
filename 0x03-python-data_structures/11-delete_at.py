#!/usr/bin/python3
"""delete_at(): a function that deletes the item at
                a specific position in a list.
    my_list=[]: list to be handled
    idx: index to be mainipulated
            (with default value set to 0)
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return(my_list)
    del my_list[idx]
    return my_list
