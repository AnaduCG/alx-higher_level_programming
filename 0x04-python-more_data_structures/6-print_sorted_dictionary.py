#!/usr/bin/python3
"""
"""


def print_sorted_dictionary(a_dictionary):
    sort_dic = {k: a_dictionary[k] for k in sorted(a_dictionary.keys())}
    for key, value in sort_dic.items():
        print("{:s}: {}".format(key, value))
