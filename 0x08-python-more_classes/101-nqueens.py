#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    print('N must be an integer greater or equal to 4')
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if n < 4:
    print('N must be at least 4')
    sys.exit(1)

board = [[-1 for _ in range(n)] for _ in range(n)]


def is_attacking(x, y):
    """Check if a queen at (x, y) is attacking another queen."""
    for i in range(n):
        if board[i][y] == 1 or board[x][i] == 1:
            return True
    for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
        if board[i][j] == 1:
            return True
    for i, j in zip(range(x, n), range(y, -1, -1)):
        if board[i][j] == 1:
            return True
    return False


def solve(row):
    """Solve the N queens problem using backtracking."""
    for col in range(n):
        if not is_attacking(row, col):
            board[row][col] = 1
            if row < n - 1:
                solve(row + 1)
                board[row][col] = 0
            else:
                print(board)


solve(0)
