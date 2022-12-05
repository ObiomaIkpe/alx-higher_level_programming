#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_end = len(row) - 1
        for i in range(len(row)):
            print("{:d}".format(row[i]), end=" " if i != row_end else "")
        print("")
