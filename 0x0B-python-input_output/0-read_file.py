#!/usr/bin/python3
''' Module that contains a function '''


def read_file(filename=""):
    ''' Function that reads a file '''
    with open(filename, "r", encoding="utf-/") as my_file:
        for line in my_file:
            print(line, end="")
