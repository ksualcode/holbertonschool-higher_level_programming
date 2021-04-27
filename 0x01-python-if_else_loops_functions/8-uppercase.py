#!/usr/bin/python3
def uppercase(str):
    for char in str:
        to_char = ord(char)
        if to_char >= 97 and to_char <= 122:
            to_char = to_char - 32
        print("{:c}".format(int(to_char)), end='')
    print()
