#!/usr/bin/python3
import math
"""magig class"""


class MagicClass:
    """calculate area and circumference"""

    def __init__(self, radius=0):
        self.___radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        return self.___radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return ((2 * math.pi) * self.__radius)
