#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    Nromans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) != str:
        return(0)
    for i in roman_string:
        if i in roman_string:
            nget = Nromans.get(i)
            num = num + nget
    return(num)
