#!/usr/bin/python3
for x in range(100):
    print('{:02d}, '.format(x), end='')
    if x == 99:
        print('{:d}\n'.format(x), end='')
