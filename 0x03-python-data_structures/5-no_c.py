#!/usr/bin/python3
"""no_c() - a function that removes all characters
            c and C from a string
    my_string: string to be handled by the function
"""


def capital(my_string):
    return my_string.translate({ord('C'): None})


def no_c(my_string):
    return capital(my_string).translate({ord('c'): None})
