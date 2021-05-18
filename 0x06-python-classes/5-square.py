#!/usr/bin/python3
''' Square class that has a getter'''


class Square:
    """ A square class """
    def __init__(self, size=0):
        """ The constructor of SQUARE class """
        self.__size = size

    def area(self):
        """ Calculates the area of the square """
        return self.__size ** 2

    @property
    def size(self):
        """ getter of the value size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of the value size """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")

        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ setter of the value size """
        n = self.__size
        if (n == 0):
            print()
        else:
            for i in range(n):
                for j in range(n):
                    print("#", end="")
                print()
