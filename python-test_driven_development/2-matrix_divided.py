#!/usr/bin/python3
"""Defines a matrix division function.

matrix_divided(matrix, div) divides every element of a matrix by a
number, validating the matrix shape and the divisor first.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimals.

    Raises TypeError for a bad matrix or div, ZeroDivisionError if div is 0.
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(all(isinstance(n, (int, float)) for n in row)
                    for row in matrix)):
        raise TypeError(err)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
