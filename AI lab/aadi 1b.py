def isSafe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQueens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueens(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack

    return False

def printBoard(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def solveQueens():
    N = 8
    board = [[0] * N for _ in range(N)]
    if not solveNQueens(board, 0):
        print("Solution does not exist")
        return False

    printBoard(board)
    return True

# Run the solver
solveQueens()
