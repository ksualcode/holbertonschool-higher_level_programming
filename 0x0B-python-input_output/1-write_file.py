#!/usr/bin/python3
''' Module that contains a function '''


def write_file(filename="", text=""):
    ''' Function that writes in a file '''
    with open(filename, "w", encoding="utf-/") as my_file:
        my_file.write(text)
