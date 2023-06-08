#!/usr/bin/python3.8
def hd():
    from hidden_4 as hidden
    hidden_names = dir(hidden)
    hidden_names = sorted(hidden_names)
    for i in hidden_names:
        if i[0] != '_':
            print("{}".format(hidden_names))


if __name__ == "__main__":
    hd()
