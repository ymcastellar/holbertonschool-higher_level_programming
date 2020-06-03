#!/usr/bin/python3
"""[Read file]
"""


def read_file(filename=""):
    """[read_file]

    Keyword Arguments:
        filename {str} -- [description] (default: {""})
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        for line in f:
            print(line, end="")
    f.close()
