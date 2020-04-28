#!/usr/bin/python3m

def print_last_digit(number):
    lastdig = abs(number) % 10
    print("{:d}".format(lastdig), end='')
    return(lastdig)
