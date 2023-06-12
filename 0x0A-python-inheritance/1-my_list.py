#!/usr/bin/python3
""" Creating Mylist class """


class MyList(list):
    """
    MyList class that inherits from base clase(list)
    """
    def print_sorted(self):
        """
        Prints the sorted list
        """
        print(sorted(self))
