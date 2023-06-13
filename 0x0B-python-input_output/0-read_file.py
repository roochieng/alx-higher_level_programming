#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it out"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it out"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
