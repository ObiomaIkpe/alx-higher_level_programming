#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_of_items = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i], end=""))
        except (ValueError, TypeError):
            pass
        return (num_of_items)
