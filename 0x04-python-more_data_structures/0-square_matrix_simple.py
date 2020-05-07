#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square(x):
        return x ** 2
    sq = []
    for i in range(len(matrix)):
        sq.append(list(map(square, matrix[i])))

    return(sq)
