#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) == 1:
        print("0 arguments.")
    else:
        print("{} argument".format(len(arguments)-1), end ='')
        if len(arguments) != 2:
            print("s:")
        else:
            print(":")
        for args in range(1, len(arguments)):
            print("{}: {}".format(args, arguments[args]))
