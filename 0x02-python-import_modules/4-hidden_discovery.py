#!/usr/bin/python3.8
def hd():
    from hidden_4 as hidden
    hidden_names = dir(hidden)
    for i in hidden_names:
        print("{}".format(hidden_names))


if __name__ == "__main__":
    hd()
