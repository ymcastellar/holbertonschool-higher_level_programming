#!/usr/bin/python3
def fizzbuzz():
    for i in range (1, 101):
        mul3 = i % 3
        mul5 = i % 5
        if mul3 == 0 and mul5 == 0:
            print("FizzBuzz", end=' ')
        elif mul3 == 0:
            print("Fizz", end=' ')
        elif mul5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')
