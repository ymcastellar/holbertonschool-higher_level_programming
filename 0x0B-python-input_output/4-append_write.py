#!/usr/bin/python3
"""[Append to a file]
"""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="UTF8") as f:
        New_F = f.write(text)
    f.close()
    return New_F
