#!/usr/bin/python3
"""[Number of lines]
"""


def number_of_lines(filename=""):
    line = 0
    with open(filename) as f:
        for i in f:
            line += 1
    f.close()
    return line
