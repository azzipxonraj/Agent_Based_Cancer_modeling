import environment
from environment import create_grid, place_tumor
from gui import game_loop

row_size = 50
col_size = 50

def main():
    game_loop(row_size, col_size)


if __name__ == '__main__':
    main()
