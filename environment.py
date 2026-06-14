import random

def create_grid(rows, cols):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    return grid

def copy_grid(grid):
    copied_grid = [row[:] for row in grid]
    return copied_grid

def place_tumor(grid, rows, cols):
    row = random.randint(0, rows - 1)
    col = random.randint(0, cols - 1)
    grid[row][col] = 2
    return grid


def cell_environment():
    pass

def time_loop(t, grid):
    count = 0
    while count <= t:
        new_grid = copy_grid(grid)
        for row_idx, row in enumerate(grid):
            for col_idx, cel in enumerate(row):
                if cel == 2:





            pass
        count += 1