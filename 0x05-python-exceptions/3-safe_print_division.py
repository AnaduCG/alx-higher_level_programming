#!/usr/bin/python3
def safe_print_division(a, b):
    """a function that divides 2 integers and prints the result.

    Args:
        a (int)
        b (int)
    """
    try:
        div = a/b
    except ZeroDivisionError:
        div = None
    except ValueError:
        div = None
    except TypeError:
        div = None
    finally:
        print("inside result{}".format(div))
