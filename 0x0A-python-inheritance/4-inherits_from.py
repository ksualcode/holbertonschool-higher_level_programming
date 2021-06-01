#!/usr/bin/python3
''' Moore modules with just one function '''


def inherits_from(obj, a_class):
    ''' Checks if it's a class or a baseclass object '''
    return issubclass(type(obj), a_class) and not type(obj) == a_class
