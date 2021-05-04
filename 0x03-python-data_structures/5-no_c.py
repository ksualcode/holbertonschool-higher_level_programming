#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for n in my_string:
        if not (n == 'c' or n == 'C'):
            new_string = new_string + n

    return new_string
