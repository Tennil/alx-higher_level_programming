#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_dt = abs(number) % 10

if number < 0:
    last_dt *= -1
if last_dt > 5:
    print(f"Last digit of {number} is {last_dt} and is greater than 5")
elif last_dt == 0:
    print(f"Last digit of {number} is {last_dt} and is 0")
else:
    print(f"Last digit of {number} is {last_dt:} and is less than 6 and not 0")

