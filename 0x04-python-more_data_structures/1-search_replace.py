#!/usr/bin/python3
"""search_replace - function that replaces all occurrences
                    of an element by another in a new list.
   @my_list: is the initial list
   @search: is the element to replace in the list
   @replace: is the new element
"""


def search_replace(my_list, search, replace):
    return list(replace if i == search else i for i in my_list)
