#!/usr/bin/python3
" Module that creates a rectangle "


class Rectangle:
    """
    Creates a rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor method """
        self.width = width
        self.height = height
        self.number_of_instances += 1

    def __del__(self):
        """ Delete method """
        print("Bye rectangle...")
        self.number_of_instances -= 1

    def __str__(self):
        """ Prints a rectangle """
        square = ""

        if self.__width == 0 or self.__height == 0:
            return square

        for i in range(self.height):
            square += str(self.print_symbol) * self.width
            if i != self.height - 1:
                square += "\n"

        return square

    def __repr__(self):
        """ Returns a string representation """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    @property
    def height(self):
        """ Getter of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ Getter of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ Calculates the area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Calculates the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Evaluates and returns which rectangle is bigger """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
