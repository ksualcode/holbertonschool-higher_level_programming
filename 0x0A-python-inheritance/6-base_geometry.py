#!/usr/bin/python3
''' Module with an empty class '''


class BaseGeometry():
    """ Class that's a superclass """

    def area(self):
        ''' raises an exception '''
        raise Exception("area() is not implemented")
