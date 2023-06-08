#!/usr/bin/python3
def infite():
    import sys
    j = 0
    for i in sys.argv[1:]:
        j += int(i)
    print(j)


if __name__ == "__main__":
    infite()
