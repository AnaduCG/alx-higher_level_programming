#!/usr/bin/python3
def f_calc():
    from calculator_1 import *
    a = 10
    b = 5
    print("10 + 5 = {}".format(add(a, b)))
    print("10 - 5 = {}".format(sub(a, b)))
    print("10 * 5 = {}".format(mul(a, b)))
    print("10 / 5 = {}".format(div(a, b)))


if __name__ == "__main__":
    f_calc()
