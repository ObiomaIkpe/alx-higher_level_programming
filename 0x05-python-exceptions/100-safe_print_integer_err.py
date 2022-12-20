#!/usr/bin/python3

import sys
import os


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
    else:
        return True
