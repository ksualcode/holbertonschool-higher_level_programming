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

    def update(self, *args, **kwargs):
        ''' Updates a Square '''
        if args is not None and len(args) != 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 3:
                self.x = args[2]
            if len(args) > 4:
                self.y = args[3]

        elif kwargs is not None:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs["y"]
