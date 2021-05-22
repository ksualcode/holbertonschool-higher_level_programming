#!/usr/bin/python3
"""Executable command
    Say_my_name fuction
"""


def say_my_name(first_name, last_name=""):
    """print a name
        usage: say_my_name(str, str)
    """

    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    if (type(last_name) != str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
