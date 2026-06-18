import random
T_GROWTH_CHANCE = 0.3

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

def get_neighbours(grid, row_idx, col_idx):
    neighbours = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        new_row = row_idx + dr
        new_col = col_idx + dc
        if new_row < 0 or new_row >= len(grid):
            continue
        if new_col < 0 or new_col >= len(grid[new_row]):
            continue
        neighbours.append((new_row,new_col))
    return neighbours



def cell_environment():
    pass

def time_loop(t, grid):
    count = 0
    while count <= t:
        new_grid = copy_grid(grid)
        for row_idx, row in enumerate(grid):
            for col_idx, cel in enumerate(row):
                if cel == 2:
                    neighbour_row, neighbour_col = random.choice(get_neighbours(grid, row_idx, col_idx))
                    if new_grid[neighbour_row][neighbour_col] != 2:
                        new_grid[neighbour_row][neighbour_col] = 2
                if cel == 1:
                    neighbour_row, neighbour_col = random.choice(get_neighbours(grid, row_idx, col_idx))

                if cel == 0:
                    neighbour_row, neighbour_col = random.choice(get_neighbours(grid, row_idx, col_idx))
        count += 1