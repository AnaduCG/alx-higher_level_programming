#!/usr/bin/python3
def b_calculator():
    import sys
    arg = sys.argv

    if len(arg) != 4:
        print("Usage: {} <a> <operator> <b>".format(arg[0]))
        exit(1)
    a = arg[1]
    b = arg[3]
    sn = arg[2]
    if sn == '+':
        print("{} + {} = {}".format(a, b, a + b))
    elif sn == '-':
        print("{} - {} = {}".format(a, b, a - b))
    elif sn == '*':
        print("{} * {} = {}".format(a, b, a * b))
    elif sn == '/':
        print("{} / {} = {}".format(a, b, a / b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    b_calculator()
