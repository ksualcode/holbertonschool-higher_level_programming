#!/usr/bin/python3
''' Module that has a class that inherits from list '''


class MyList(list):
    """ Class that prints a list sorted """

    def print_sorted(self):
        ''' Prints the sorted list '''
        print(sorted(self))
