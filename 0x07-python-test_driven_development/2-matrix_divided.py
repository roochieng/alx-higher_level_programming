#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """ Defining the matric dividion 
    matrix is a list of list of integers, else raise TypeError
    and a message of matrix must be a matrix (list of lists)
    of integers/floats.
    Each row must be same size, else raise TypeError:
    with message: Each row of the matrix must have the same size
    div must be number(float or int), else raise TypeError:
    with message: div must be a number
    div can't be equal to 0 else raise ZeroDivisionError
    with message: division by zero
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
