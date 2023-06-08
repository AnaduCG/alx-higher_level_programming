#!/usr/bin/python3
import sys
if(len(sys.argv) <= 1):
    print("{} argument:".format(len(sys.argv) - 1))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
for i, j in enumerate(sys.argv[1:], start=1):
    print("{}: {}".format(i, j))
