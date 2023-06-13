#!/usr/bin/python3
"""Function for JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """Return JSON representation of an object (string)"""
    return json.dumps(my_obj)
