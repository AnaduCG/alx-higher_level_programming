#!/usr/bin/python3
import sys

def safe_function(fct, *args):
        """ a function that executes a function safely

        Args:
            fct (poinrt):  a pointer to a function

        Returns:
            any: Returns the result of the function,
            Otherwise, returns None if something happens during the
            function and prints in stderr the error precede by Exception:
        """
        try:
                return fct(*args)
        except Exception as err:
                sys.stderr.write("Exception: {}\n".format(err))
                return None
