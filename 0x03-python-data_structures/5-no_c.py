#!/usr/bin/python3

def no_c(my_string):

    new_string = ""
    for char in my_string:
        new_string += "" if char =="c" or char == "C" else char
    my_string = new_string
    del new_string
    return (my_string)
