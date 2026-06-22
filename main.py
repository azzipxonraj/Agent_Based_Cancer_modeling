import environment
from environment import create_grid, place_tumor, time_loop

row_size = 50
col_size = 50

def main():
    grid = create_grid(row_size, col_size)
    grid_t = place_tumor(grid, row_size, col_size)
    print(time_loop(100, grid_t))

if __name__ == '__main__':
    main()
