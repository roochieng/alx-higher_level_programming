#!/usr/bin/python3
""" Creat a square class """


class Square:
    """ Define a class square """
    def __init__(self, size=0):
        """ Initializing a square class
        Argguments: size=0: size of the square
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
