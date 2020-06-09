#!/usr/bin/python3
"""[And now, the Square!]
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """[class Square that inherits from Rectangle]
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ stdout 
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def arg_update(self, id=None, size=None, x=None, y=None):
        """ update square
        """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ update square using args
        """
        if args:
            self.arg_update(*args)
        elif kwargs:
            self.arg_update(**kwargs)

    def to_dictionary(self):
        """ return a dictionary
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
