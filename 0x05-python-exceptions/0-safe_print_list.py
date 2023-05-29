#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(my_list):
	    print(i, sep="")
	    x += 1
	    number += 1
            for x in range(number):
                print("", end="")
        print()
	return number
    except IndexError:
        print()
        return number
