#!/usr/bin/python3
''' Square class that has a getter'''


class Square:
    """Square class with all attributes"""
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """Constructor of square"""
        self.size = size
        self.position = position

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Size getter"""
        return (self.__size)

    @property
    def position(self):
        """Getter of position"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Set the position of a square"""
        if (type(value) != tuple or len(value) != 2 or
                type(value[0]) != int or value[0] < 0 or
                type(value[1]) != int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Method that prints a square"""
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
