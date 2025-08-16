from typing import List, Optional, Tuple

Grid = List[List[int]]

def find_empty(grid: Grid) -> Optional[Tuple[int, int]]:
    """Return (row,col) of the next empty cell (0), or None if solved."""
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None

def is_valid(grid: Grid, r: int, c: int, val: int) -> bool:
    """Check if placing val at (r,c) keeps the Sudoku constraints."""
    # Row and column
    if any(grid[r][x] == val for x in range(9)): return False
    if any(grid[x][c] == val for x in range(9)): return False
    # 3x3 box
    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if grid[i][j] == val:
                return False
    return True

def solve_sudoku(grid: Grid) -> bool:
    """
    Solve the Sudoku in-place using backtracking.
    Returns True if a solution exists, otherwise False.
    """
    empty = find_empty(grid)
    if not empty:
        return True  # solved
    r, c = empty
    for val in range(1, 10):
        if is_valid(grid, r, c, val):
            grid[r][c] = val
            if solve_sudoku(grid):
                return True
            grid[r][c] = 0  # backtrack
    return False

def pretty_print(grid: Grid) -> None:
    """Print the Sudoku grid with box separators."""
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        row_chunks = []
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row_chunks.append("|")
            row_chunks.append(str(grid[r][c]) if grid[r][c] != 0 else ".")
        print(" ".join(row_chunks))

if __name__ == "__main__":
    # 0 denotes empty cells
    puzzle = [
        [0,0,0, 2,6,0, 7,0,1],
        [6,8,0, 0,7,0, 0,9,0],
        [1,9,0, 0,0,4, 5,0,0],

        [8,2,0, 1,0,0, 0,4,0],
        [0,0,4, 6,0,2, 9,0,0],
        [0,5,0, 0,0,3, 0,2,8],

        [0,0,9, 3,0,0, 0,7,4],
        [0,4,0, 0,5,0, 0,3,6],
        [7,0,3, 0,1,8, 0,0,0],
    ]

    print("Input:")
    pretty_print(puzzle)
    print("\nSolving...\n")

    if solve_sudoku(puzzle):
        print("Solved:")
        pretty_print(puzzle)
    else:
        print("No solution exists.")
