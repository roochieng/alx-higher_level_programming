#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(sys.argv[0]))
	print("{}: ".format(argc), sys.argv[1])
    else:
        print(argc, "arguments:")
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))
