#!/usr/bin/python3
"""Defines a function `read_file`"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
