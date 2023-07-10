#!/usr/bin/python3


class MyList(list):
    """class that inherits from list class

    Args:
        list (class): class that contains a list of integers
    """

    def print_sorted(self):
        """MyList method that prints a list in sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)
