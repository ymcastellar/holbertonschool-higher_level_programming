#!/usr/bin/python3
"""[Write to a file]
"""


def write_file(filename="", text=""):
    """[write_file]
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        New_F = f.write(text)
    f.close()
    return New_F
