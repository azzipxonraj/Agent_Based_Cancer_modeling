import random
T_GROWTH_CHANCE = 0.003342937006
C_DOUBLING_TIME = 0.2928932188

def create_grid(rows, cols):
    grid = [[1 for _ in range(cols)] for _ in range(rows)]
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



def time_loop(t, grid_t):
    count = 0
    tumor_history = []
    while count <= t:
        new_grid = copy_grid(grid_t)
        for row_idx, row in enumerate(grid_t):
            for col_idx, cel in enumerate(row):
                if cel == 2:
                    neighbour_row, neighbour_col = random.choice(get_neighbours(grid_t, row_idx, col_idx))
                    if new_grid[neighbour_row][neighbour_col] != 2 and random.random() < T_GROWTH_CHANCE:
                        new_grid[neighbour_row][neighbour_col] = 2
                if cel == 1:
                    neighbour_row, neighbour_col = random.choice(get_neighbours(grid_t, row_idx, col_idx))
                    if new_grid[neighbour_row][neighbour_col] == 0 and random.random() < C_DOUBLING_TIME:
                        new_grid[neighbour_row][neighbour_col] = 1
        tumor_history.append(sum(1 for row in new_grid for cel in row if cel == 2))
        count += 1
        grid_t = new_grid
    return new_grid, tumor_history

