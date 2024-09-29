#!/usr/bin/python3
""" This is a 2D matrix to rotate it 90 degrees
clockwise"""


def rotate_2d_matrix(matrix):
    """ This is the function that will take the
    n matrix and will return the clockwise rotation
    of the matrix"""
    t_matrix = zip(*matrix)
    for row in t_matrix:
        return row
