#!/usr/bin/python3
"""[Geometry module]
"""


class BaseGeometry:
    """[Improve Geometry]
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """[Rectangle that inherits from BaseGeometry ]
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        Rectangle.integer_validator(self, "width", self.__width)
        Rectangle.integer_validator(self, "height", self.__height)

    def __str__(self):
        string = "["+ str(self.__class__.__name__) +"] {}/{}" .format(self.__width, self.__height)
        return string

    def area(self):
        return self.__width * self.__height
