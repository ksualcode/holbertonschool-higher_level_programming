#!/usr/bin/python3
''' Module that contains a function '''


def append_write(filename="", text=""):
    ''' Function that appends text to a file '''
    with open(filename, "a", encoding="utf-/") as my_file:
        my_file.write(text)
