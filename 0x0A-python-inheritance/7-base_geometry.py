#!/usr/bin/python3
''' Module with an empty class '''


class BaseGeometry:
    ''' A Base Geometry class '''
    def area(self):
        ''' the area of the shape '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validates an int value '''
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
