import random
from setup import parse_args
args = parse_args()


T_GROWTH_CHANCE = args.tumor_growth_chance
C_DOUBLING_TIME = args.c_doubling_time
TUMOR_HISTORY = []

def create_grid(rows, cols):
    # grid gets made and filled with healthy cells
    grid = [[1 for _ in range(cols)] for _ in range(rows)]

    # realistically a cellular sample is never complete and tidy this code introduces a random amount of empty space.
    for row in range(rows):
        if row < random.randint(0,8):
            for col in range(cols):
                grid[row][col] = 0
                grid[row * -1][col * -1] = 0

        else:
            # For the side of the sample
            for col in range(cols):
                if col < random.randint(0,8):
                    grid[row][col] = 0
                    grid[row * -1][col* -1] = 0
    return grid

def copy_grid(grid):
    # this new grid is used to apply the simulation changes for
    copied_grid = [row[:] for row in grid]
    return copied_grid

def place_tumor(grid, rows, cols):
    # we want to place the tumor within the allowed rows and columns
    row = random.randint(0, rows - 1)
    col = random.randint(0, cols - 1)
    grid[row][col] = 2
    return grid

def get_neighbours(grid, row_idx, col_idx):
    # We want to get all the neighbours of the cell (except diagnolly for now)
    neighbours = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # we will check for these directions
    for dr, dc in directions:
        new_row = row_idx + dr
        new_col = col_idx + dc
        if new_row < 0 or new_row >= len(grid):
            continue
        if new_col < 0 or new_col >= len(grid[new_row]):
            continue
        neighbours.append((new_row,new_col))
    return neighbours


def do_single_time_step(grid_t):
    new_grid = copy_grid(grid_t)
    # This is what the so called rules are for each agent
    for row_idx, row in enumerate(grid_t):
        for col_idx, cel in enumerate(row):
            # what to do if the cell is a tumor
            if cel == 2:
                neighbours = get_neighbours(grid_t, row_idx, col_idx)
                if neighbours:
                    neighbour_row, neighbour_col = random.choice(neighbours)
                    if new_grid[neighbour_row][neighbour_col] != 2 and random.random() < T_GROWTH_CHANCE:
                        new_grid[neighbour_row][neighbour_col] = 2
            # what to do if a cell is healthy
            if cel == 1:
                neighbours = get_neighbours(grid_t, row_idx, col_idx)
                if neighbours:
                    neighbour_row, neighbour_col = random.choice(neighbours)
                    if new_grid[neighbour_row][neighbour_col] == 0 and random.random() < C_DOUBLING_TIME:
                        new_grid[neighbour_row][neighbour_col] = 1
    TUMOR_HISTORY.append(sum(1 for row in new_grid for cel in row if cel == 2)) # tumor history for latter analysis
    return new_grid