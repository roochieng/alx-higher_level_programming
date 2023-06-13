#!/usr/bin/python3
"""
Add all arguments to a Python list,
and then save them to a file.
"""


from json import dumps


def save_to_json_file(my_obj, filename):
    """Add all arguments to a Python list and save to a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
