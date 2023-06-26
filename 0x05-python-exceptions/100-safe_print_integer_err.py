#!/user/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer value and handles exceptions.
    Args:
        value (any): The value to be printed.
    Returns:
        bool: True if the value is an integer and printed
        successfully, False otherwise.
    """
    err = "Exception: Unknown format code 'd' for object of type 'str'\n"
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        sys.stderr.write("{}".format(err))
        return False
