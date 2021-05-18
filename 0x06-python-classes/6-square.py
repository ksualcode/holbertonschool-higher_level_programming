#!/usr/bin/python3
"""In this module you will find a class
"Square" at the moment it does nothing"""


class Square:
    """In this class we save a data"""
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """This is the constructor of the class"""
        self.size = size
        self.position = position

    def area(self):
        """This function return area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """This property get size"""
        return (self.__size)

    @property
    def position(self):
        """This property get position"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """This property set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """This property set position"""
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or value[0] < 0 or
                type(value[1]) != int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """This function print square"""
        if (self.__size == 0):
            print()
            return
        for i in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
