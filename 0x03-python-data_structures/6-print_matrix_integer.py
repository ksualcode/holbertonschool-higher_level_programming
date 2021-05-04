#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            print(i[j], end='')
            if j != len(i) - 1:
                print("", end=' ')
        print()
