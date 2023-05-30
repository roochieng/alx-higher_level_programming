#!/usr/bin/python3
""" Create a square class """


class Square:
    """ Define a class square """
    def __init__(self, size=0):
        """ Initializing a square class
        Arguments: size=0: size of the square
         """
        self.__size = size

    @property
    def size(self):
        """ Get the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate the area of the square """
        return (self.__size ** 2)

    def my_print(self):
        """ Print the square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
