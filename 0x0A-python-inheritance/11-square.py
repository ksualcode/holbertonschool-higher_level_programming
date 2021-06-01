#!/usr/bin/python3
''' Module with an empty class '''


Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    def __init__(self, size):
        ''' Constructor of the function '''
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        ''' Calculates the area of a square '''
        return self.__size ** 2

    def __str__(self):
        ''' Prints a rectangle '''
        return "[Square] {}/{}".format(self.__size, self.__size)
