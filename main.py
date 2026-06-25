from gui import game_loop
from setup import parse_args

args = parse_args()

# gompertz test values
N_max = args.rows * args.cols
b = 7.8240
c = 0.0004481


def main():
    game_loop(args.rows, args.cols, args.max_steps, N_max, b, c)


if __name__ == '__main__':
    main()
