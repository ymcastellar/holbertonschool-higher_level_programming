#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    con = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            con = con + 1
        except IndexError:
            break
    print()
    return con
