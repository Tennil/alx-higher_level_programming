#!/usr/bin/python3

for z in range(0, 100):
    if z < 99:
        print("{:02d}".format(z), end=", ")
    else:
        print("{:02d}".format(z))
