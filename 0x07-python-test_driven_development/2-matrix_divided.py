#!/usr/bin/python3
"""
Module: matrix_divided
"""


def matrix_divided(matrix, div):
    """Divides a matrix
    """
    new_matrix = []
    error8 = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(error8)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix[0]:
        length = len(matrix[0])

    else:
        raise TypeError(error8)

    for i in range(len(matrix)):
        if len(matrix[i]) is not length:
            raise TypeError("Each row of the matrix must have the same size")

        new_matrix.append([])

        for j in matrix[i]:
            if type(j) is int or type(j) is float:
                new_matrix[i].append(round(j / div, 2))

            else:
                raise TypeError(error8)

    return new_matrix
