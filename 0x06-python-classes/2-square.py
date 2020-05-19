#!/usr/bin/python3
""" class that defines a square """


class Square:
    """ ---builder to define size---

        Args: size: size of square.

        """
    def __init__(self, size=0):
        self.__size = size

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
