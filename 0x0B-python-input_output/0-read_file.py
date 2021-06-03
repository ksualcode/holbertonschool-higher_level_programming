#!/usr/bin/python3
''' Module that contains a function '''


def read_file(filename=""):
    ''' Function that reads a file '''
    with open(filename, "r", encoding="utf-/") as my_file:
        print (my_file.read())
