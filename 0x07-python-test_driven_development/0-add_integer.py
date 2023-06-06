#!/usr/bin/python3

"""
Function that takes two integers

Add and return their int sum
"""

def add_integer(a, b=98):
    """ Check the numbers if float or int
    Add and return their int summation
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
