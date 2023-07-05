#!/usr/bin/python3
"""
    module documentation
"""

def print_square(size):
    """ prints a square with the character #"""

    if type(size) is not an int:
        raise TypeError("size must be an integer")
    if type(size) < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")
    for num in range(size):
        for i in range(size):
            print('#', end="")
        print()
