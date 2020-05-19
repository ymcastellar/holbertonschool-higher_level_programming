#!/usr/bin/python3
""" class that defines a square """


class Square:
    """ ---builder to define size---

        Args: size: size of square.

        """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    """area - return the the square area"""

    def area(self):
        return (self.__size ** 2)
