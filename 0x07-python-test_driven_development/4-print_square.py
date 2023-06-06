#!/usr/bin/python3
""" A function that prints a square of #."""


def print_square(size):
    """A function that prints a square of #."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
