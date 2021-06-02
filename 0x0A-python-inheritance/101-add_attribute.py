#!/usr/bin/python3
''' Advanced Module '''


def add_attribute(obj, attr, value):
    ''' Function that adds a new attribute '''
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)

    raise TypeError("can't add new attribute")
