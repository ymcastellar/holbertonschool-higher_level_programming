#!/usr/bin/python3
def islower(c):
    number = ord(c)
    if number > 96 and number < 123:
        return True
    elif number > 64 and number < 91:
        return False
