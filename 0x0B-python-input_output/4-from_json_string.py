#!/usr/bin/python3
"""Defines a function ``from_json_string``"""
import json


def from_json_string(my_str):
    """Returns the decoded object of @my_str JSON string"""
    return (json.loads(my_str))
