#!/usr/bin/python3
''' Module with the square class '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Superclass for other classes '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Class constructor '''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        ''' size getter '''
        return self.__width

    @size.setter
    def size(self, size):
        ''' size setter '''
        super().value_validator(size, "width")
        self.__width = size
        self.__height = size
