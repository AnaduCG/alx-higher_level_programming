#!/usr/bin/python3
"""add_tuple() - a fucntion that adds two tupples
    tuple_a=(): the tupple for the addition
    tuple_b=(): the tupple for the addition
"""


def add_tuple(tuple_a=(), tuple_b=()):
    ta = list(tuple_a)
    tb = list(tuple_b)
    if len(ta) < 1:
        ta.append(0)
    if len(ta) < 2:
        ta.append(0)
    if len(tb) < 1:
        tb.append(0)
    if len(tb) < 2:
        tb.append(0)
    return (ta[0] + tb[0], ta[1] + tb[1])
