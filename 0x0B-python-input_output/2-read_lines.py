#!/usr/bin/python3
"""[Read n lines]
"""


def read_lines(filename="", nb_lines=0):
    """[read_lines]
    """
    line = 0
    with open(filename, mode="r", encoding="UTF8") as f:
        for i in open(filename):
            line += 1
        if nb_lines <= 0 or nb_lines >= line:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
    f.close()
