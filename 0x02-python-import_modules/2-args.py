#!/usr/bin/python3
def sys_arg():
    import sys
    sys.argv.pop(0)
    if len(sys.argv) == 1:
        print("{:d} argument:".format(len(sys.argv)))
    else:
        print("{:d} arguments:".format(len(sys.argv)))
    for i in range(len(sys.argv)):
        print("{:d}: {:d}".format(i + 1, sys.argv[i]))


if __name__ == "__main__":
    sys_arg()
