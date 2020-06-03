#!/usr/bin/python3
"""[Read file]
"""


def read_file(filename=""):
    with open(filename,mode="r", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
    f.close()
