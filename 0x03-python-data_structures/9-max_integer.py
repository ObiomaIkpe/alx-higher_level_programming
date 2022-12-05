#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""
    if (not my_list):
        return (None)
    max_num = my_list[0]
    list_len = len(my_list)

    for num in my_list:
        if num > max_num:
            max_num = num

    return (max_num)
