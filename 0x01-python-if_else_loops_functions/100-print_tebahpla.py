#!/usr/bin/python3
for length in range(0, 26):
    word = ord('z') - length
    if (length % 2 == 1):
        word = chr(word - ord('a') + ord('A'))
    else:
        word = chr(word)
    print("{}".format(word), end='')
