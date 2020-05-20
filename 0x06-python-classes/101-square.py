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
        if not isinstance(self.position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(self.position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(self.position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    """area - return the the square area"""

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.size > 0:
            if self.position[1] > 0:
                for newline in range(self.position[1]):
                    print("")
            for row in range(self.size):
                if self.position[0] > 0:
                    for spaces in range(self.position[0]):
                        print(" ", end="")
                for collumn in range(self.size):
                    print("#", end="")
                print("")
        else:
            print("")
