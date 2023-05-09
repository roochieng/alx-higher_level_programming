#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
strnum = str(number)
last = strnum[-1]
last = int(last)
if last[-1] > 5:
    print(f"Last digit of {number} is {number[-1]} and is greater than 5")
elif last[-1] == 0:
    print(f"Last digit of {number} is {number[-1]} and is 0")
elif last[-1] < 6 and last[-1] != 0:
    print(f"Last digit of {number} is {number[-1]} and is less than 6 and not 0")
