#!/usr/bin/python3
''' Creates a class '''


class Square:
    """ A square class """
    def __init__(self, size=0):
        """ The constructor of SQUARE class """
        try:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
