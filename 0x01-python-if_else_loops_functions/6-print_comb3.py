#!/usr/bin/python3
for i in range(10):
    for j in range(10-i-1):
        if i == 8 and j+i+1 == 9:
            print("{:d}{:d}".format(i, j+i+1))
            break
        print("{:d}{:d}".format(i, j+i+1), end=', ')
