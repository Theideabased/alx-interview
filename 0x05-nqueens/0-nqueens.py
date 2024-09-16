#!/usr/bin/python3

import sys

result = []


def issafe(board, row, column, n):
    """
    the will take the 2D matrix and make sure that
    the queen is placed in the place that is not being
    attack by another queen
    """
    # this will check the first row
    for i in range(column):
        if board[row][i]:
            return False

    # This will check the left upper diagonal
    i = row
    j = column
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # This will check the right upper diagonal
    i = row
    j = column
    while j >= 0 and i < n:
        if board[i][j]:
            return False
        j -= 1
        i += 1
    return True


def placethequeen(board, col, n):
    """
    this will place the queen in the right place
    so that one queen will not be attacking the other queen
    """
    # The base case
    if (col == n):
        v = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    v.append([i, j])
        result.append(v)
        return True

    res = False
    for i in range(n):
        if (issafe(board, i, col, n)):
            board[i][col] = 1
            res = placethequeen(board, col+1, n) or res
            # backtracking
            board[i][col] = 0
    return False


def nqueens(N):
    """
    this will call all the function that is necessary and
    print them out as needed
    """
    result.clear()
    board = [[0 for j in range(n)] for i in range(n)]
    placethequeen(board, 0, N)
    result.sort()
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        else:
            res = nqueens(n)
            for solutions in res:
                print(solutions)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
