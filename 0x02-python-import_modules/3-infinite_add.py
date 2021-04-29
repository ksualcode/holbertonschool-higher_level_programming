#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv
    n = 0
    for arg in range(1, len(args)):
        n = n + int(args[arg])
    print(n)
