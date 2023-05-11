#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv
    result = 0

    for i in range(1, argc):
        result = result + int(argv[i])

    print(result)
