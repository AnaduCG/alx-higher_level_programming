#!/usr/bin/python3.8
def hd():
    import hidden_4

    names = dir(hidden_4)
    names.sort()
    for name in names:
        if name[0] != '_':
            print("{}".format(name))


if __name__ == "__main__":
    hd()
