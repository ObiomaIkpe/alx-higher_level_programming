#!/usr/bin/python3
def uppercase(str):
    for c in str:
        charCode = ord(c)
        if charCode >= 97 and charCode <= 122:
            c = chr(charCode - 32)
        print("{}".format(c), end="")
    print("")
