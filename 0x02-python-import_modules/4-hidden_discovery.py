#!/usr/bin/python3.8
def hd():
    from hidden_4 as hidden
    names = dir(hidden)
    hidden_names = sorted(names for name in names if not name.startswith('_'))
    for i in hidden_names:
            print("{}".format(hidden_names))


if __name__ == "__main__":
    hd()
