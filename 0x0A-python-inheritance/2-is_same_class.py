#!/usr/bin/python3
""" Funtion that returns true if the object is an instance of a class """


def is_same_class(obj, a_class):
    """
    Return true if the object is an instance of its class
    """
    return type(obj) == a_class
