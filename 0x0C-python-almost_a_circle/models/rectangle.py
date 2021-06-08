#!/usr/bin/python3
''' Module with the rectangle class '''
from models.base import Base


class Rectangle(Base):
    ''' Superclass for other classes '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Class constructor '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # Setters and Getters
    @property
    def width(self):
        """ Getter of width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter of width """
        self.value_validator(width, "width")
        self.__width = width

    @property
    def height(self):
        """ Getter of height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter of height """
        self.value_validator(height, "height")
        self.__height = height

    @property
    def x(self):
        """ Getter of x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter of x """
        self.value_validator(x, "x")
        self.__x = x

    @property
    def y(self):
        """ Getter of y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter of y """
        self.value_validator(y, "y")
        self.__y = y

    # end of getters / setters

    def area(self):
        ''' Returns the area of a Rectangle'''
        return self.__width * self.__height

    def display(self):
        ''' Prints the rectangle'''
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        ''' Updates a Rectangle '''
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

        elif kwargs is not None:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        ''' prints '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    @staticmethod
    def value_validator(value, name):
        ''' Validates a given value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def to_dictionary(self):
        ''' Returns the dictionary of a Rectangle '''
        new_dict = {'id': self.id, 'width': self.width,
                    'height': self.height, 'x': self.x, 'y': self.y}
        return new_dict
