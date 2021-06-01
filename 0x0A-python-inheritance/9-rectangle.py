#!/usr/bin/python3
''' Module with an empty class '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        ''' Constructor of the function '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' Calculates the area of a square '''
        return self.__width * self.__height

    def __str__(self):
        ''' Prints a rectangle '''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
