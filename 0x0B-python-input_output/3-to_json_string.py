#!/usr/bin/python3
"""Defines a function `to_js0n_string`"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of @my_obj

    Args:
        my_obj (object): object to be used
    """
    return (json.dumps(my_obj))
