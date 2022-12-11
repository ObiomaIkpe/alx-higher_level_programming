#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

last_digit = number % 10
if number < 0:
    last_digit = last_digit - 10

if last_digit > 5:
    str = "greater than 5"
elif last_digit == 0:
    str = "0"
else:
    str = "less than 6 and not 0"
print("Last digit of {} is {} and is {}".format(number, last_digit, str))
