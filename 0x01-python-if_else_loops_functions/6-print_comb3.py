#!/usr/bin/python3

for j in range(0, 10):
    for k in range(0, 10):
        if j == 8 and k == 9:
            print("{:d}{:d}".format(j, k))
        elif j < k and j != k:
            print("{:d}{:d},".format(j, k), end='')
