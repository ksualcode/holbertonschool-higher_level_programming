#!/usr/bin/python3
''' Module with an empty class '''


Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """ Class that inherits the rectangle class """

    def __init__(self, size):
        ''' Constructor of the function '''
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        ''' Calculates the area of a square '''
        return self.__size ** 2
