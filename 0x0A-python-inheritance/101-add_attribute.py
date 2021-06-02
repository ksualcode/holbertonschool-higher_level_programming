#!/usr/bin/python3
''' Advanced Module '''


def add_attribute(obj, attr, value):
    ''' Function that adds a new attribute '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
