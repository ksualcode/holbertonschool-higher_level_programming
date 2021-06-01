#!/usr/bin/python3
''' Another module with just one function '''


def is_kind_of_class(obj, a_class):
    ''' Checks if it's a class or a baseclass object '''
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
