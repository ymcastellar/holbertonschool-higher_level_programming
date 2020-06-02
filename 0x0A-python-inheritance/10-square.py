#!/usr/bin/python3
"""[Geometry module]
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """[Square that inherits from Rectangle]
    """

    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)
    
    def __str__(self):
        string = "[Rectangle] {}/{}" .format(self.__size, self.__size)
        return string
        
        
