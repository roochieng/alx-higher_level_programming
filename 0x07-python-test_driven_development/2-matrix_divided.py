#!/usr/bin/python3

""" Function that divides matrix """


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
    tmplist = []
    if all(isinstance(elem, list) for elem in matrix) == False:
        raise TypeError("matrix must be a matrix (list of lists) 
	of integers/floats")

    for a in len(matrix):
        for b in len(matrix[a - 1]):
	    if type(matrix[a - 1][b - 1]) != int or
	    type(matrix[a - 1][b - 1]) != int:
	        raise TypeError("matrix must be a matrix (list of lists)
		of integers/floats")
	    b += 1
	a += 1

    for i in len(matrix):
        if len(matrix[i]) != len(matrix[i - 1]:
	    raise TypeError("matrix must be a matrix (list of lists) 
	    of integers/floats")
	i += 1

    if type(div) != int or type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for k in range(matrix) - 1:
        for l in matrix[k] - 1:
	    num = round(l/div, 2)
	    tmplist = tmplist.append(num)
	    l += 1
	k += 1
	tmplist = tmplist.append(matrix)
    return(tmplist)
