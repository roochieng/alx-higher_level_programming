#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    elems = len(my_list) -1
    while elems !< 0:
        print("{:d}".format(my_list[elems]]))
	elems -= 1
