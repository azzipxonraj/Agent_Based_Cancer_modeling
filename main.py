from gui import game_loop

row_size = 50
col_size = 50
max_steps = 200

# gompertz test values
N_max = row_size * col_size
b = 7.8240
c = 0.0004481


def main():
    game_loop(row_size, col_size, max_steps, N_max, b, c)


if __name__ == '__main__':
    main()
