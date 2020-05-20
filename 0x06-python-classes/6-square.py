#!/usr/bin/python3
""" class that defines a square """


class Square:
    """ ---builder to define size---

        Args: size: size of square.

        """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        if type(self.__position) is not tuple or len(value) != 2:
           raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    """area - return the the square area"""

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        list = []
        for i in range(self.__size):
            list.append("#" * self.__size)
        print(*list, sep="\n")
