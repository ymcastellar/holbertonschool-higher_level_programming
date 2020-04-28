#!/usr/bin/python3
def print_last_digit(number):
    lastdig = abs(number) % 10
    print("{:d}".format(lastdig), end='')
    return(lastdig)
