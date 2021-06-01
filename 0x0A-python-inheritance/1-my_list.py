#!/usr/bin/python3
''' Module that has a class that inherits from list '''


class MyList(list):
    def print_sorted(self):
        ''' Prints the sorted list '''
        print(sorted(self))
