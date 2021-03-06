#!/usr/bin/python3
''' Square class with an init condition '''


class Square:
    """ A square class """
    def __init__(self, size=0):
        """ The constructor of SQUARE class """

        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")

        elif (size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
