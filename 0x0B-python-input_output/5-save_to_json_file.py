#!/usr/bin/python3
"""Defines a function ``save_to_json``"""
import json


def save_to_json_file(my_obj, filename):
    """Writes @my_obj to @filename using JSON representation.

    Args:
        my_obj (object): object to be converted
        filename (file): destination file to be written
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
