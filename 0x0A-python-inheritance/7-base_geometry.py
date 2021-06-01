#!/usr/bin/python3
''' Module with an empty class '''


class BaseGeometry():
    """ Class that's a superclass """
    def area(self):
        ''' raises an exception '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Validates the value that comes in '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
