#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv
    n = 0
    for arg in range(1, len(args)):
        n = n + int(args[arg])
    print(n)
