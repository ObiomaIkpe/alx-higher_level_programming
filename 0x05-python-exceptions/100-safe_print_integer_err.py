#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        write(2, "Exception: {}\n".format(err).enocode("utf-8"))
        return (False)
    else:
        return True
