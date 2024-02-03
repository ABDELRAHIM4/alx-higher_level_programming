import sys
def is_safe(board, row, col):
    n = len(board)

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, col):
    n = len(board)

    if col >= n:
        print(board)
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1

            solve(board, col + 1)

            board[i][col] = 0

def nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    solve(board, 0)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = int(sys.argv[1])

    if not isinstance(n, int) or n < 4:
        print("N must be a number")
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
