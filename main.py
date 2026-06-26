from gui import game_loop
from setup import parse_args

args = parse_args()

# gompertz test values
N_max = args.rows * args.cols



def main():
    game_loop(args.rows, args.cols, args.max_steps, N_max, args.b, args.c)


if __name__ == '__main__':
    main()
