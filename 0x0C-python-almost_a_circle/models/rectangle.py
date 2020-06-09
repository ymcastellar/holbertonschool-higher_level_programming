#!/usr/bin/python3
"""[First Rectangle ]
"""
from models.base import Base


class Rectangle(Base):
    """[Class Rectangle inherits from Base]

    Args:
        base ([type]): [class]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """[height getter]
        """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ x stter
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """[y getter]
        """
        return self.__y

    @y.setter
    def y(self, y):
        """[y setter]

        Args:
            y ([type]): [description]

        Raises:
            TypeError: [must be an integer]
            ValueError: [must be > 0]
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """get area
        """
        return self.__height * self.__width

    def display(self):
        """[display]
        """
        for nl in range(self.y):
            print()
        for ht in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for wt in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """stdout
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def arg_update(self, id=None, width=None, height=None, x=None, y=None):
        """[arg_update]
        """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ update
        """
        if args:
            self.arg_update(*args)
        elif kwargs:
            self.arg_update(**kwargs)

    def to_dictionary(self):
        """to dictionary
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
